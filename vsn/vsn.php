<?php
/*
Plugin Name: VSN Tarot
Description: Interactive tarot card reader.
Version: 0.1
Author: Codex
*/

if ( ! defined( 'ABSPATH' ) ) exit;

class VSN_Tarot {
    public function __construct() {
        add_action( 'init', [ $this, 'register_post_type' ] );
        add_action( 'rest_api_init', [ $this, 'register_routes' ] );
        add_shortcode( 'vsn_tarot', [ $this, 'render_shortcode' ] );
        add_action( 'wp_enqueue_scripts', [ $this, 'enqueue_scripts' ] );
    }

    public function register_post_type() {
        register_post_type( 'vsn_card', [
            'label' => 'Tarot Cards',
            'public' => false,
            'show_ui' => true,
            'supports' => [ 'title', 'thumbnail', 'editor' ],
        ] );

        register_taxonomy( 'vsn_category', 'vsn_card', [
            'label' => 'Tarot Categories',
            'public' => false,
            'show_ui' => true,
            'hierarchical' => false,
        ] );
    }

    public function register_routes() {
        register_rest_route( 'vsn/v1', '/draw', [
            'methods' => 'GET',
            'callback' => [ $this, 'api_draw' ],
            'permission_callback' => '__return_true',
        ] );
    }

    public function api_draw( $request ) {
        $category    = sanitize_key( $request->get_param( 'category' ) );
        $cookie_name = 'vsn_card_' . ( $category ? $category : 'default' );
        $post        = null;

        if ( ! empty( $_COOKIE[ $cookie_name ] ) ) {
            list( $card_id, $date ) = explode( '|', $_COOKIE[ $cookie_name ] );
            if ( $date === date( 'Y-m-d' ) ) {
                $post = get_post( (int) $card_id );
            }
        }

        if ( ! $post ) {
            $args = [
                'post_type'      => 'vsn_card',
                'posts_per_page' => 1,
                'orderby'        => 'rand',
            ];
            if ( $category ) {
                $args['tax_query'] = [
                    [
                        'taxonomy' => 'vsn_category',
                        'field'    => 'slug',
                        'terms'    => $category,
                    ],
                ];
            }
            $query = new WP_Query( $args );
            if ( empty( $query->posts ) ) {
                return new WP_Error( 'no_cards', 'No cards found', [ 'status' => 404 ] );
            }
            $post = $query->posts[0];
            setcookie( $cookie_name, $post->ID . '|' . date( 'Y-m-d' ), time() + DAY_IN_SECONDS, COOKIEPATH, COOKIE_DOMAIN );
        }

        $data = [
            'id'      => $post->ID,
            'title'   => $post->post_title,
            'image'   => get_the_post_thumbnail_url( $post->ID, 'large' ),
            'content' => apply_filters( 'the_content', $post->post_content ),
        ];
        return rest_ensure_response( $data );
    }

    public function render_shortcode( $atts = [] ) {
        $atts = shortcode_atts( [ 'mode' => 'daily' ], $atts );
        $mode = esc_attr( $atts['mode'] );
        ob_start();
        ?>
        <div id="vsn-tarot" data-mode="<?php echo $mode; ?>">
            <button class="vsn-draw">Draw Card</button>
            <div class="vsn-card" style="display:none;"></div>
        </div>
        <?php
        return ob_get_clean();
    }

    public function enqueue_scripts() {
        wp_enqueue_script( 'vsn-tarot', plugin_dir_url( __FILE__ ) . 'vsn.js', [ 'jquery' ], '0.1', true );
        wp_localize_script( 'vsn-tarot', 'VSN_TAROT', [
            'api' => rest_url( 'vsn/v1/draw' ),
        ] );
        wp_enqueue_style( 'vsn-tarot', plugin_dir_url( __FILE__ ) . 'vsn.css', [], '0.1' );
    }
}
new VSN_Tarot();
?>

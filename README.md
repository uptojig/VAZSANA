# VSN Tarot Plugin

This repository contains the beginnings of the **VSN** (Very Spiritual Now) WordPress plugin. It provides a minimal interactive tarot card reader using a custom post type and a REST API.

The plugin now supports fortune-telling categories (daily, 3-6 months, love, career, finance, health, luck and education). Use these categories to organise your cards and control which deck is drawn from.

## Installation

1. Copy the `vsn` folder into your WordPress `wp-content/plugins` directory.
2. Activate **VSN Tarot** from the plugins screen.
3. Add tarot cards using the **Tarot Cards** menu in the WordPress admin. Assign each card to one or more **Tarot Categories**.
4. Embed the reader on any page with the shortcode:

```
[vsn_tarot mode="daily"]
```

## Development Notes

- Card data can be imported from `tarot.xlsx`.
- The shortcode attribute `mode` selects which category to draw from. Example:
  ```
  [vsn_tarot mode="finance"]
  ```
- Each visitor can draw one card per category per day.

jQuery(function($){
    var container = $('#vsn-tarot');
    var mode = container.data('mode');
    var drawn = false;
    container.on('click', '.vsn-draw', function(){
        if(drawn) return;
        $.get(VSN_TAROT.api, {category: mode}).done(function(res){
            container.find('.vsn-card').html('<h3>'+res.title+'</h3><img src="'+res.image+'" /><div>'+res.content+'</div>').show();
            drawn = true;
        });
    });
});

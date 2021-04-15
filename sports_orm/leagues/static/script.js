$(document).ready(function(){


    $('.player').hover(function(){
        console.log("Player clicked")
        $(this).children().css( "display", "block" )
        },
        function(){
            $(this).children().css( "display", "none" )
        }
    );


});

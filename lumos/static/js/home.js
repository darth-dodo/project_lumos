$(document).ready(function(){
    $(".massive").hover(function () {
        // $(this).transition("bounce");
        $(this).toggleClass("inverted")
     });

    $("#love").hover(function () 
        {$(".heart").css({"color": "red"});}, 
        function () 
        {$(".heart").css({"color": "white"}); 
    });

    $(document).on('click', '#disclaimer', function(event) {
        event.preventDefault();
        $('#disclaimer-modal').modal('show');
    });

    $(document).on('click', '#feedback', function(event) {
        event.preventDefault();
        $('#feedback-modal').modal('show');
    });


});//document ready
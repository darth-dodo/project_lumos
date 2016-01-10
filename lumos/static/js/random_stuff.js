$(document).ready(function(){
$(".stuff").hover(function () {
    stuff_id = ($(this).data("id"));
    $(this).toggleClass("inverted")
    $("#stuff_"+stuff_id).show();
        },
    function(){
        $("#stuff_"+stuff_id).hide();
        $(this).toggleClass("inverted") 
      });

});//document ready
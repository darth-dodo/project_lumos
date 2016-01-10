$(document).ready(function(){

  $('.diff_lvl_0').addClass("inverted green");
  $('.diff_lvl_1').addClass("inverted yellow");
  $('.diff_lvl_2').addClass("inverted orange");
  
  $(".row_data").hover(function () {  
    // $(this).transition("bounce");
    $(this).toggleClass("inverted ")
 });

$("#feedback").click(function(){
$('#feedback-modal').modal('show');
})

});//document ready
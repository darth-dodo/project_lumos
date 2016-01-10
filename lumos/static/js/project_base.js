$(document).ready(function(){
$('.diff_lvl_0').addClass("inverted green");
$('.diff_lvl_1').addClass("inverted yellow");
$('.diff_lvl_2').addClass("inverted orange");

$(".project").hover(function () {
    project_id = ($(this).data("id"));
    $(this).toggleClass("inverted")
    $("#project_id_"+project_id).show();
        },
    function(){
        $("#project_id_"+project_id).hide();
        $(this).toggleClass("inverted") 
      });

});//document ready
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
    });


    $(".csvClass").click(function() {
        var location_url = document.URL;
        var url_arr = location_url.split("/");
        // url is "/http://projectlumos.pythonanywhere.com/technical/knowledge-base/"
        var location_slug = url_arr[url_arr.length - 1]
        console.log(location_slug);
        window.open('/csv_gen/'+location_slug,'_blank');
        // fetchCsv(location_slug);
    });

});//document ready
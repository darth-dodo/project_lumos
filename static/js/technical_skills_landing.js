$(document).ready(function(){

    $(".skill").hover(function () {
        $(this).toggleClass("inverted red")
     });

    $(".csvClass").click(function() {
        var location_url = document.URL;
        var url_arr = location_url.split("/");
        // url is "/http://projectlumos.pythonanywhere.com/technical/knowledge-base/"
        var location_slug = url_arr[url_arr.length - 2]
        console.log(location_slug);
        window.open('/csv_gen/'+location_slug,'_blank');
    });

});//document ready
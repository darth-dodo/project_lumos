$(document).ready(function(){

    function fetchCsv(location_slug){
        console.log(location_slug);
        data = {'location_slug': location_slug};

        $.ajax({
            url: '/csv-generation/',
            type: 'POST',
            data: data
        });//ajax
        
    }//fetchCsv


    $(".skill").hover(function () {
        // $(this).transition("bounce");
        $(this).toggleClass("inverted red")
     });

    $(".csvClass").click(function() {
        var location_url = document.URL;
        var url_arr = location_url.split("/");
        // url is "/http://projectlumos.pythonanywhere.com/technical/knowledge-base/"
        var location_slug = url_arr[url_arr.length - 2]
        console.log(location_slug);
        window.open('/csv_gen/'+location_slug,'_blank');
        // fetchCsv(location_slug);
    });

});//document ready
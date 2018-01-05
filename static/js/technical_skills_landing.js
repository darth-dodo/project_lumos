$(document).ready(function(){

    (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
      (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
      m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
      })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

      ga('create', 'UA-86912923-1', 'auto');
      ga('send', 'pageview');

      ga('require', 'ec');

    $(".skill").hover(function () {
        // $(this).transition("bounce");
        $(this).toggleClass("inverted red")
     });

    $(".csvClass").click(function() {
        var location_url = document.URL;
        var url_arr = location_url.split("/");
        // url is "/http://projectlumos.pythonanywhere.com/technical/knowledge-base/"
        var location_slug = url_arr[url_arr.length - 2]
        window.open('/csv_gen/'+location_slug,'_blank');
    });

    $(".skill").click(function(){
            var skill = $(this).text()
            ga('ec:addProduct', {
              'id': 'P12345',
              'name': skill
              'category': 'Apparel',
              'brand': 'Google',
              'variant': 'black'
            });

            ga('ec:setAction', 'detail');
            }
        )
});//document ready
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

	$("#disclaimer").click(function(){
		$('#disclaimer-modal').modal('show');
	})

	$("#feedback").click(function(){
		$('#feedback-modal').modal('show');
	})

	
});//document ready
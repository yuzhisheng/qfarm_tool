$(document).ready(function(){

	console.log($(".sidebar"))
	console.log($("#nav"))
	$("a.mobile").click(function(){
		$(".sidebar").slideDown('fast');
	});

	$("a.menuclose").click(function(){
		$(".sidebar").slideUp('fast');
	});

    $('#nav li').click(function() {
    	$('#nav li').removeClass('selected');
    	$(this).addClass('selected');
    	console.log($(this).index())
	    $.getJSON('/getPage', {
	    	index: $(this).index()
	      }, function(data) {
	      	console.log("getPage" + data.result)
	        $("#content").html(data.result)
	      });
    });		
	

	window.onresize = function(event){
		if($(window).width() > 730){
			$(".sidebar").show();
		}
	};

	function mhweb_relocate() {
    var window_top = $(window).scrollTop();
    var div_top = $('#mhwebhold').offset().top;
    if (window_top > div_top) {
        $('#hold').addClass('glue');
        $('#mhwebhold').height($('#hold').outerHeight());

    } else {
        $('#hold').removeClass('glue');
        $('#mhwebhold').height(0);
    }
	}

	$(function() {
	    $(window).scroll(mhweb_relocate);
	    mhweb_relocate();

	});

});


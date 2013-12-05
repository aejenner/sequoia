$(document).ready(function(){
 //do stuff
 
	$("#toRegister").click(function(){
		//hide login div, show register
		$('#login').css({'display':'none'});
		$('#register').show("blind",800);
		//$('#register').css({'display':'block'});
	});
	
	$("#toLogin").click(function(){
		//hide register show login
		$('#register').css({'display':'none'});
		$('#login').show("blind",800);
		//$('#login').css({'display':'block'});
	});
	
	//more "user friendly" way to confirm password... hit a button to show it
	$(".showpassword").each(function (index, input) {
    var $input = $(input);
    $("button").click(function () {
      var change = "";
      if ($(this).html() === "Show Password") {
        $(this).html("Hide Password")
        change = "text";
      } else {
        $(this).html("Show Password");
        change = "password";
      }
      var rep = $("<input type='" + change + "' />")
        .attr("id", $input.attr("id"))
        .attr("name", $input.attr("name"))
        .attr('class', $input.attr('class'))
		.attr("required", $input.attr('required'))
        .val($input.val())
        .insertBefore($input);
      $input.remove();
      $input = rep;
    }).insertAfter($input);
	});
	
 
 
 
 
 
 
});
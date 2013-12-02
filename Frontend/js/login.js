$(document).ready(function(){
 //do stuff
 
	$("#toRegister").click(function(){
		//hide login div, show register
		$('#login').css({'display':'none'});
		$('#register').show("blind",650);
		//$('#register').css({'display':'block'});
	});
	
	$("#toLogin").click(function(){
		//hide register show login
		$('#register').css({'display':'none'});
		$('#login').show("blind",650);
		//$('#login').css({'display':'block'});
	});
 
 
 
 
 
 
});
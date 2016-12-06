$(function() {

    $('#login-form-link').click(function(e) {
		$("#loginForm").delay(100).fadeIn(100);
 		$("#registerForm").fadeOut(100);
		$('#register-form-link').removeClass('active');
		$(this).addClass('active');
		e.preventDefault();
	});
	$('#register-form-link').click(function(e) {
		$("#registerForm").delay(100).fadeIn(100);
 		$("#loginForm").fadeOut(100);
		$('#login-form-link').removeClass('active');
		$(this).addClass('active');
		e.preventDefault();
	});

});

$("#registerForm").validate({
           rules: {
               password: { 
                 required: true,
                    minlength: 6,
                    maxlength: 64,

               } , 

                   confirm-password: { 
                    equalTo: "#password",
                     minlength: 6,
                     maxlength: 64
               }


           },
     messages:{
         password: { 
                 required:"The entered passwords do not match."

               }
     }

});


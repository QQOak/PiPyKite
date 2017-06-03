'use strict';
$(document).ready(function(){	
	
	
	$('#takePicture').click(function() {
		
		// Send a request to the server to request a picture be taken
		// The response will incude the filename and path of the image taken.
		var jqXHR = $.getJSON("/api/camera/takepicture")
		.done(function( data ) {
			//alert('done');
			//var obj = $.parseJSON(data);
			//alert(data.filename);
			//alert(data.filename);
			$('#pictureTaken').css("background-image", "url(/"+ data.filename +")");
			
		})
		.fail(function( jqxhr, textStatus, error) {
			//alert('fail');
			//alert(textStatus);
			//alert(error);
			//alert(jqxhr);
		})
		.always(function(){
			//alert('always');
		})

	});
	
});

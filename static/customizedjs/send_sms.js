$(document).ready(function() {
	$("#Button2").click(function(event) {
			event.preventDefault();
			var username = $("#Username").val();
			var password = $("#Password").val();
			var sendto = $("#sendto").val();
			var description = $("#description").val();
			if (username != '' && password != '' && sendto != '' && description!=''){
				$('.alert').show();
					window.setTimeout(function() {
							$(".alert").fadeTo(500, 0).slideUp(500, function() {
									$(this).remove();
							});
							location.reload()
					}, 2000);
			}
					
			$.ajax({
					url: "http://127.0.0.1:8000/user/sendsms",
					type: "POST",
					data: {
							'username': username,
							'password': password,
							'sendto': sendto,
							'description': description,
					},
					dataType: "json",
					success: function(response) {
							if (response.error=="error") {
								$('.alert').show();
								window.setTimeout(function() {
							$(".alert").fadeTo(500, 0).slideUp(500, function() {
									$(this).remove();
							});
							location.reload()
					}, 2000);
									
							}
					},
					error: function(err) {
							// alert("Error");
							return false;
					}
			});
	});
});
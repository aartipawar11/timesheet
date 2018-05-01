$(document).ready(function() {
		$("#adduserform").submit(function(event) {
				event.preventDefault();
				// var el = document.getElementsByName("csrfmiddlewaretoken");
				// csrf_value = el[0].getAttribute("value");
				$.ajax({
						url: "http://127.0.0.1:8000/user/",
						type: "POST",
						data: {
								'first_name': $("#first_name").val(),
								'last_name': $("#last_name").val(),
								'dob': $("#dob").val(),
								'gender': $("#gender:checked").val(),
								'email': $("#email").val(),
								'password': $("#password").val(),
								'designation': $("#designation").val(),
								'role': $("#role:checked").val(),
								// 'csrfmiddlewaretoken':csrf_value
						},
						dataType: "json",
						success: function(response) {
								if (response) {
										console.log(response);
										$('.alert').show();
										window.setTimeout(function() {
												$(".alert").fadeTo(500, 0).slideUp(500, function() {
														$(this).remove();
												});
												location.reload()
										}, 2000);
										if (response.status == 201) {
												alert("User Created Successfully!");
												window.location = "admindashboard";
										}
										if (response.status == 404) {
												console.log("Error in creating user")
												alert("Error in creating user")
										};

								}
						},
						dataType: "json",
						success: function(response) {
								if (response) {
										console.log(response);

										if (response.status == 201) {
												alert("User Created Successfully!");
												window.location = "admindashboard";
										}
										if (response.status == 404) {
												console.log("Error in creating user")
												alert("Error in creating user")
										};

								}
						},
						error: function(err) {
								// alert("Error");
								return false;
						}

				});

		});
});
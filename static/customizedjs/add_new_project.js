$(document).ready(function() {
		$("#createprojectform").submit(function(event) {
				event.preventDefault();
				// var el = document.getElementsByName("csrfmiddlewaretoken");
				// csrf_value = el[0].getAttribute("value");
				$.ajax({
						url: "http://127.0.0.1:8000/project/",
						type: "POST",
						data: {
								'name': $("#projectname").val(),
								'description': $("#projectdescription").val(),
								// 'csrfmiddlewaretoken':csrf_value
						},
						dataType: "json",
						success: function(response) {
								if (response) {
										console.log(response);
										$('.alert').show();
										// alert("Details updated  ")
										window.setTimeout(function() {
												$(".alert").fadeTo(500, 0).slideUp(500, function() {
														$(this).remove();
												});
												location.reload()
										}, 2000);
										if (response.status == 201) {
												alert("Project Created Successfully!");
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
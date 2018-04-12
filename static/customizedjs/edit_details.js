$(document).ready(function() {
        $("#userdetailform").submit(function(event) {
            event.preventDefault();
            var id = getCookie("id");
            var user = getCookie("user");

            var role = getCookie("role");
            var url = "http://127.0.0.1:8000/user/" + id;
            $.ajax({
                url: url,
                type: "PUT",
                data: {
                    'first_name': $("#first_name").val(),
                    'last_name': $("#last_name").val(),
                    'mobile': $("#mobile").val(),
                    'dob': $("#dob").val(),
                    'gender': $("#gender").val(),
                    'id': getCookie("id"),
                    'user': getCookie("user"),
                    'role': getCookie("role"),
                    'designation': $("#designation").val(),


                },
                dataType: "json",
                success: function(response) {
                    if (response) {
                        console.log(response);
                        alert("Details updated  ")


                        if (response.status == 200) {
                            alert("User Created Successfully!");
                            console.log("response 200 coming");
                        }
                        if (response.status == 404) {
                            console.log("Error in Getting user details")
                            alert("Error in creating user")
                        }

                    }
                },
                error: function(err) {
                    // alert("Error");
                    return false;
                }

            });
        });

    });


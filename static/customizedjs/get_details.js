 $(document).ready(function(event) {
        var userid = getCookie("id");
        var url = "http://127.0.0.1:8000/user/" + userid;
        $.ajax({
            url: url,
            type: "GET",
            dataType: "json",
            success: function(response) {
                if (response) {
                    console.log(response);
                    document.getElementById("first_name").innerHTML = response.first_name;
                    document.getElementById("last_name").innerHTML = response.last_name;
                    document.getElementById("mobile").innerHTML = response.mobile;
                    document.getElementById("dob").innerHTML = response.dob;
                    document.getElementById("gender").innerHTML = response.gender;
                    document.getElementById("designation").innerHTML = response.designation;



                    if (response.status == 200) {
                        alert("Got details!");
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


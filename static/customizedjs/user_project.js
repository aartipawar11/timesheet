$(document).ready(function() {
    $("#adduserform").submit(function(event) {
        event.preventDefault();
        var el = document.getElementsByName("csrfmiddlewaretoken");
        csrf_value = el[0].getAttribute("value");
        $.ajax({
            url: "http://127.0.0.1:8000/user/assignproject",
            type: "POST",
            data: {

                'inputEmail': $("#projectList").val(),
                'inputPassword': $("#Password").val(),
                'csrfmiddlewaretoken': csrf_value
            },
            dataType: "json",
            success: function(response) {
                if (response) {
                    // console.log(response);
                    setCookie("Authorization","Token" + response.token);
                    setCookie("id", response.user);
                    // setCookie("", response.role);


                    // if(response.role==3){
                    //   $("#alertmesg").hide();
                    //   $("#alertsuccess").show();
                    //   $("#alertsuccess").html("Login Successfully");
                    //   window.location = "dashboard";
                    // }
                    // if(response.role==2){
                    //   $("#alertmesg").hide();
                    //   $("#alertsuccess").show();
                    //   $("#alertsuccess").html("Login Successfully");
                    // }
                    // if(response.role==1){
                    //   $("#alertmesg").hide();
                    //   $("#alertsuccess").show();
                    //   $("#alertsuccess").html("Login Successfully");
                    //   window.location = "admindashboard";
                    // }
                    if (response.status == "404") {
                        $("#alertsuccess").hide();
                        $("#alertmesg").show();
                        $("#alertmesg").html("Username or password does not exist");
                        return false;
                    };
                    if (response.status == "500") {
                        $("#alertsuccess").hide();
                        $("#alertmesg").show();
                        $("#alertmesg").html("Error while login");
                        return false;
                    };

                }
                // $("#alertsuccess").hide();
                // $("#alertmesg").show();
                // $("#alertmesg").html("Error while login");
                // return false;
            },
            error: function(err) {
                $("#alertsuccess").hide();
                $("#alertmesg").show();
                $("#alertmesg").html("Something went wrong. Please try again later. ");
                return false;
            }

        });

    });
});
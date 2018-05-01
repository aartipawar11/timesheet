   $(document).ready(function(event) {
      
        var el = document.getElementsByName("csrfmiddlewaretoken");
              csrf_value = el[0].getAttribute("value");
        var url = "http://127.0.0.1:8000/user/viewprojects";
        $.ajax({
            url: url,
            type: "POST",
            data:{
               'csrfmiddlewaretoken':csrf_value
            },
            dataType: "json",
            success: function(resp) {
                if (resp) {
                    console.log(resp);
                    var len=resp.projects.length;
                    var trHTML = '';
                    console.log(len)
                    for(i=0;i<len;i++){

                      trHTML +=
                                    '<tr><td>'
                                    + resp.projects[i].id
                                    + '</td><td>'
                                    + resp.projects[i].name
                                    + '</td><td>'
                                    + resp.projects[i].description 
                                    + '</td><td>'
                                    + resp.projects[i].created_at
                                    + '</td></tr>';
                   
                    }
                    $('#tBody').append(trHTML);
                    



                    if (resp.status == 200) {
                        alert("Got details!");
                        console.log("response 200 coming");
                    }
                    

                }
            },
            error: function(err) {
                // alert("Error");
                return false;
            }

        });

    });
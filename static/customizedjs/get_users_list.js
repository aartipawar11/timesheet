 $(document).ready(function() {
        var url = "http://127.0.0.1:8000/user/";
        
        $.ajax({
            url: url,
            type: "GET",
            dataType: "json",
             success:function(resp){
               var len=resp.length;
               console.log(len)
               var trHTML = '';
                        // $.each(resp, function (i) {
                            for (i = 0; i < len; i++) {
                                trHTML +=
                                    '<tr><td>'
                                    + resp[i].id
                                    + '</td><td>'
                                    + resp[i].first_name 
                                    + '</td><td>'
                                    + resp[i].last_name 
                                    + '</td><td>'
                                    + resp[i].role_name 
                                    + '</td></tr>';
                            }
                        // });
                        $('#tBody').append(trHTML);
                    },
                    error: function (req, status, err) { 
                        console.log('something went wrong', status, err);
                    }
                })
            });
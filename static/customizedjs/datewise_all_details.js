$(document).ready(function(event) {
		var urls = $(location).attr('href'),
		value = urls.split("/"),
 		user_id = value[value.length-1];
		var url = "http://127.0.0.1:8000/task/edittask";
        $.ajax({
            url: url,
            type: "POST",
            dataType: "json",
            success: function(response) {
               console.log(response);
               var len = response.length;
                for (i = 0; i < len; i++) {
                  var trHTML = '';
                     if (response[i].user == user_id) {
                         var project = response[i].project; 
                            trHTML +=
                                      '<tr><td>'
                                      + response[i].user
                                      + '</td><td>'
                                      + response[i].date
                                      + '</td><td>'
                                      + response[i].project_name
                                      + '</td><td>'
                                      + response[i].billing_description
                                      + '</td><td>'
                                      + response[i].billing_hour
                                      + '</td><td>'
                                      + response[i].id
                                      + '</td><td>'
                                      + response[i].non_billing_description
                                      + '</td><td>'
                                      + response[i].non_billing_hour
                                      + '</td><td>'
                                      + response[i].total_hour
                                      + '</td></tr>';
                        
                     }
                     $('#tBody').append(trHTML);
                 };
            },
            error: function(err) {
                return false;
            }

        });

    });

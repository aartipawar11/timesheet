
       $(document).ready(function(event) {
        var userid = getCookie("user");
        var url = "http://127.0.0.1:8000/task/calculate_hours/"+userid;
        $.ajax({
            url: url,
            type: "GET",
            success: function(response) {
              if(response){
               var total_billing_hour= "00:00";
               var total_non_billing_hour= "00:00";
               for(i=0;i<response.length;i++){
                total_billing_hour=addTimes(total_billing_hour,response[i].billing_hour);
                total_non_billing_hour=addTimes(total_non_billing_hour,response[i].non_billing_hour);
               }
               
                //Calclute Hrs start here
              
              function timeToMins(time) {
                var b = time.split(':');
                return b[0]*60 + +b[1];
              }
              function timeFromMins(mins) {
                function z(n){return (n<10? '0':'') + n;}
                var h = (mins/60 |0) % 24;
                var m = mins % 60;
                return z(h) + ':' + z(m);
              }
              function addTimes(t0, t1) {
                return timeFromMins(timeToMins(t0) + timeToMins(t1));
              }
                //Calclute Hrs ends here

               document.getElementById('billhrs').innerHTML= total_billing_hour;
               document.getElementById('nonbillhrs').innerHTML= total_non_billing_hour;
               }
            },
            error: function(err) {
                return false;
            }
        });
    });

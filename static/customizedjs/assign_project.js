
$(document).ready(function(){
             $("#Button2").click(function(event){
              event.preventDefault();
                var nn=$('#test').val();
               alert(nn);
              var el = document.getElementsByName("csrfmiddlewaretoken");
              csrf_value = el[0].getAttribute("value");
                 $.ajax({
                  url: "http://127.0.0.1:8000/user/assignproject",
                  type:"POST",
                     data: {
                     'project':$("#select1").val(),
                     'user':$("#select2").val(), 
                     'csrfmiddlewaretoken':csrf_value
                     },
                     dataType: "json",
                     success: function(response){
                
                        console.log(response);
                       
                     // $("#alertsuccess").hide();
                     // $("#alertmesg").show();
                     // $("#alertmesg").html("Error while login");
                     // return false;
                 },
                 error: function (err) {
                   $("#alertsuccess").hide();
                   $("#alertmesg").show();
                   $("#alertmesg").html("Something went wrong. Please try again later. ");
                   return false;
                 }
         
               });
         
             });
         });

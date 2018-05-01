
      $(document).ready(function(){
             $("#deluserform").submit(function(event){
              event.preventDefault();
              var id=$("#inputid").val();
              if(id==''){
                
                document.getElementById("inputerror").innerHTML = "No Input Provided!";
                }
                 $.ajax({
                  url: "http://127.0.0.1:8000/user/"+id,
                  type:"delete",
                     dataType: "json",
                     success: function(response){
                     if(response){
                       console.log(response);
                        $('.alert').show();
                           window.setTimeout(function() {
                           $(".alert").fadeTo(500, 0).slideUp(500, function(){
                           $(this).remove(); 
                           });
                           location.reload()
                           }, 2000);
                       }
                 },
                 error: function (err) {
                   // alert("Error");
                   return false;
                 }
         
               });
         
             });
         });

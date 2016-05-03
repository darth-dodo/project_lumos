$(document).ready(function(){

  $("#submit").click(function(){
      var proceed = true;
      $(".feedback-data").each(function(){
        $(this).css('border-color','');
        // console.log(this);
        if(!$.trim($(this).val())){ //if this field is empty
            $(this).css('border-color','red'); //change border color to red
            
            proceed = false; //set do not proceed flag
            alert("Please provide appropriate data");
            return false;
        }
        //check invalid email
        var email_reg = /^([\w-\.]+@([\w-]+\.)+[\w-]{2,4})?$/;
        // console.log($(this).val());
        if($(this).attr("name")=="email"
           && !email_reg.test($.trim($(this).val())))
        {
            $(this).css('border-color','red'); //change border color to red
            alert('Please provide valid email!');
            proceed = false; //set do not proceed flag
            return false;
        }
        });//finishing validations
      // console.log(proceed);
      if (proceed){
        var feedback_data = {}
        username = $("#username").val();
        // console.log(username);
        if (username)
              {
                feedback_data['username'] = username
              }
        else{
            feedback_data['username'] = 'Anon'
        } 
        feedback_data['email'] = $("#email").val().trim()
        feedback_data['feedback'] = $("textarea#feedback").val().trim()
        // console.log(feedback_data);
        $.ajax({
            type : 'POST',
            url : '/feedback-form/',
            data :JSON.stringify(feedback_data)
            ,dataType : "json"
            ,success : function(data){
                alert("Thanks for providing feedback! :)");
                window.location.replace('/');
            }
            ,error : function(data){
                alert("Oh shucks! Feedback not saved! Please try again!");
            }
        });//ajax call
      }
});// submit fucntion
});//document ready

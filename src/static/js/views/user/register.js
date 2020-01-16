function registerUser(btn)
{
    if(!errorFreeForm('register-form'))
    {
        alert("The input values are invalid"); 
        return; 
    }
    else 
    {
        formSubmitText(btn); 
    }
}


function checkConfirmPassword(input, compare_input_id, required_id, not_matched_id)
{
    valueRequired(input, required_id);
    booleanHidden($('#'+compare_input_id).val()==input.value, not_matched_id); 
}

function checkEmailValid(input,required_id, valid_id)
{
    var support_function = 
    {
        validEmail: function(email)
        {
            var regular_expression = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/; 
            return regular_expression.test(String(email).toLowerCase()); 

        }
    }
    valueRequired(input,required_id); 
    booleanHidden(support_function.validEmail(input.value), valid_id); 
}

function putRandomInformationTest()
{
    var name = randomString();
    var email = randomString()+ "@yopmail.com"; 
    var username = randomString(); 
    var password = randomString(); 

    var data = 
    {
        name: name,
        email: email,
        username: username,
        password: password, 
        confirm_password: password
    }; 
    console.log(data); 
    for(var field of Object.keys(data))
    {
        $("#"+field).val(data[field]); 
    }

    errors = $('#register-form .error_alert_p'); 
        
    for (var p of errors)
    {
        $(p).attr('hidden','hidden');
    }

}

function randomString()
{
    var max_length = 30; 
    var length = max_length* Math.random(); 
    max_length = Math.floor(max_length); 
    var text = "";
    var possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"; 
    for (var i = 0; i < length; i++)
        text += possible.charAt(Math.floor(Math.random() * possible.length));
    return text;
}

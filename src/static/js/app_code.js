function ajaxPost(url, data)
{
    var result = null; 
    $.ajax
    (
        {
            url: url,
            data: data, 
            async: false, 
            type: "post", 
            dataType: "text",
            success: function(success)
            {
                result = success; 
            }, 
            error: function(error)
            {
                console.log("error"); 
                result = error; 
            }
        }
    ); 
    return result; 
}

function getDataChecking(input)
{
    var data = 
    {
    }
    let name = $(input).attr('name'); 
    data[name] = input.value; 
    var form = input.form; 
    var hidden_list = $(form).find('input[type="hidden"]'); 
    for (var hidden of hidden_list)
    {
        let name = $(hidden).attr('name'); 
        data[name] = hidden.value; 
    }
    return data; 
}

function formValues(form_id)
{
    var selector = "#"+form_id + " input:not([type='button'])"; 
    var form = $(selector); 
    var data = {}; 
    form.each
    (
        element => 
        {
            let name = $(form[element]).attr("name"); 
            let value = $(form[element]).val();
            data[name] = value; 
        }
    );
    return data; 
}

function errorFreeForm(form_id)
{
    errors = $('#'+form_id+' .error_alert_p'); 
        
    for (var p of errors)
    {
        var hidden = $(p).attr('hidden'); 
        if(hidden==undefined)
        {
            return false; 
        }
    }

    return true; 
}

function formSubmitText(btn)
{
    var url = $(btn).attr('data-url'); 
    var form_id = $(btn).attr('data-form_id'); 
    var redirect = null; 
    try 
    {
        redirect = $(btn).attr('data-redirect'); 
    }
    catch{}

    var data = formValues(form_id); 
    var result = ajaxPost(url, data); 
    if(result=='true')
    {
        alert('Thank you! The action is success.'); 
        if(redirect!=null)
        {
            window.location.href = redirect; 
        }
        else 
        {
            location.reload(); 
        }
    }
    else 
    {
        alert("We are sorry, we are unable to complete this action! Please try again"); 
    }
}

function checkValueExisted(input, valid_id, result_value)
{
    var url = $(input).attr("data-url"); 
    var data = getDataChecking(input); 
    var result = ajaxPost(url, data);
    booleanHidden(result==result_value, valid_id); 
}

function valueRequired(input, p_id)
{
    value = $(input).val().trim(); 
    if(value=="")
    {
        $("#"+p_id).removeAttr('hidden'); 
    }
    else 
    {
        $("#"+p_id).attr('hidden',"hidden");
    }

}

function booleanHidden(boolean, hidden_id)
{
    if (!boolean)
    {
        $("#"+hidden_id).removeAttr('hidden'); 
    }
    else 
    {
        $("#"+hidden_id).attr('hidden', "hidden"); 
    }
}



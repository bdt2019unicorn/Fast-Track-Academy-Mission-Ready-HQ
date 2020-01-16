function checkUserLogin(btn)
{
    if(!errorFreeForm('login-form'))
    {
        alert("The input values are invalid"); 
        return; 
    }
    else 
    {
        formSubmitText(btn); 
    }
}
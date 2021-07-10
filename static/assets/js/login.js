function submitLoginInfo() {
    var username = document.getElementById('user-name-input').innerHTML;
    var password = document.getElementById('password-input').innerHTML;
    
    $.ajax({
        type: "POST",
        url: "login",
        data: {username: username, password: password}
    })
}
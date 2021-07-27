function submitLoginInfo() {
    var username = document.getElementById('user-name-input').value;
    var password = document.getElementById('password-input').value;
    
    $.ajax({
        type: 'POST',
        url: "login",
        data: {username: username, password: password},
        dataType: "text"
      });
}
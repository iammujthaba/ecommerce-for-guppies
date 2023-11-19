
document.addEventListener('DOMContentLoaded', function () {
    var signupButton = document.getElementById('signup-button');
    var signinButton = document.getElementById('signin-button');
    var registerTab = document.getElementById('register-tab');
    var signinTab = document.getElementById('signin-tab');

    signupButton.addEventListener('click', function () {
        // Activate the "Register" tab
        registerTab.click();
    });

    signinButton.addEventListener('click', function () {
        // Activate the "Sign In" tab
        signinTab.click();
    });
});


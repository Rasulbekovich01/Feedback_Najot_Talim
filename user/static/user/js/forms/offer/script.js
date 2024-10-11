document.addEventListener('DOMContentLoaded', function () {
    const signInBtn = document.getElementById('signInBtn');
    const signUpBtn = document.getElementById('signUpBtn');
    const signInForm = document.getElementById('signInForm');
    const signUpForm = document.getElementById('signUpForm');

    signInBtn.addEventListener('click', function () {
        signInForm.style.display = 'block';
        signUpForm.style.display = 'none';
        signInBtn.classList.add('active');
        signUpBtn.classList.remove('active');
    });

    signUpBtn.addEventListener('click', function () {
        signInForm.style.display = 'none';
        signUpForm.style.display = 'block';
        signUpBtn.classList.add('active');
        signInBtn.classList.remove('active');
    });

    const form = document.querySelector('forms');
    form.addEventListener('submit', function (event) {
        event.preventDefault();
        alert('Form submitted!');
    });
});

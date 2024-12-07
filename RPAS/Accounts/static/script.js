let check_box = document.querySelector('.form-check-input');
let password_input = document.querySelector('.password-input');
let text_password = document.querySelector('.show-hide-text-password')
let show = true;

check_box.addEventListener('click', ()=>{
    if (show == true){
        text_password.innerHTML = 'Show Password';
        password_input.setAttribute('type' , 'text');
        show = false;
    }
    else{
        text_password.innerHTML = 'Hide Password';
        password_input.setAttribute('type' , 'password');
        show = true;
    }
})
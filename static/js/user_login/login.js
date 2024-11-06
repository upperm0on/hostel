document.addEventListener('DOMContentLoaded', () => {
    const conf_password = document.querySelector('#id_confirm_password');
    const password = document.querySelector('#id_password')
    const button = document.querySelector('.submit_btn')
    const error_msg = document.querySelector('.error_msg');

    conf_password.addEventListener('keyup', () => {
        if (conf_password.value != password.value) {
            button.setAttribute('disabled', '')

            error_msg.innerHTML = 'The passwords do not match'
            error_msg.classList.add('text-danger')
            error_msg.classList.add('text-center')
        }
        else {
            button.removeAttribute('disabled')

            error_msg.innerHTML = ''
        }
    })
})


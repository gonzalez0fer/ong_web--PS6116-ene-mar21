document.addEventListener('DOMContentLoaded', function() {
    document.getElementById("email").addEventListener("change", check_email)
    document.getElementById("password_1").addEventListener("change", check_password)
    document.getElementById("password_2").addEventListener("change", check_password)
})

// Verificación del email introducido
function validateEmail(email) {
    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}

// Validación dinámica del email
function check_email() {
    email = document.getElementById("email").value

    if (!validateEmail(email)) {
        document.getElementById("email_error").innerHTML = "Debe introducir un email válido"
        document.getElementById("email_error").style.visibility = "visible"
    }
    else {
        document.getElementById("email_error").style.visibility = "hidden"
        document.getElementById("default_email_error").style.visibility = "hidden"
    }
}

// Validación dinámica de las contraseñas
function check_password() {
    password = event.target.value
    password_error = event.target.id + "_error"
    
    if (password == "") {
        document.getElementById(password_error).innerHTML = "Debe introducir una contraseña"
        document.getElementById(password_error).style.visibility = "visible"
    }
    else {
        document.getElementById(password_error).style.visibility = "hidden"
        document.getElementById("default_" + password_error).style.visibility = "hidden"
        document.getElementById("passwords_error").style.visibility = "hidden"
    }
}

// Validación estática al momento de enviar el formulario
function validate() {
    error = false

    email = document.getElementById("email").value
    password_1 = document.getElementById("password_1").value
    password_2 = document.getElementById("password_2").value

    if (email == "") {
        document.getElementById("email_error").innerHTML = "Debe introducir un email"
        document.getElementById("email_error").style.visibility = "visible"
        error = true
    }

    if (password_1 == "") {
        document.getElementById("password_1_error").innerHTML = "Debe introducir una contraseña"
        document.getElementById("password_1_error").style.visibility = "visible"
        error = true
    }

    if (password_2 == "") {
        document.getElementById("password_2_error").innerHTML = "Debe introducir la verificación de contraseña"
        document.getElementById("password_2_error").style.visibility = "visible"
        error = true
    }

    if (password_1 != password_2) {
        document.getElementById("passwords_error").innerHTML = "Las contraseñas deben ser iguales"
        document.getElementById("passwords_error").style.visibility = "visible"
        error = true
    }

    email_error = document.getElementById("email_error").style.visibility
    password_1_error = document.getElementById("password_1_error").style.visibility
    password_2_error = document.getElementById("password_2_error").style.visibility
    passwords_error = document.getElementById("passwords_error").style.visibility

    if (email_error == "visible" || password_1_error == "visible" || password_2_error == "visible" || passwords_error == "visible"){
        error = true
    }

    // Si existe un error en el formulario, no se envía
    if (error) {
        return false
    }
    else {
        return true
    }
}

document.getElementById("from_date").addEventListener("change", check_from_date)
document.getElementById("to_date").addEventListener("change", check_to_date)

// Validación dinámica de la fecha inicial
function check_from_date() {
    from = new Date(document.getElementById("from_date").value);
    from_date = new Date(from.getFullYear(), from.getMonth(), from.getDate() + 1)
    today = new Date();

    if (from_date > today) {
        document.getElementById("from_error").innerHTML = "Debe introducir una fecha inicial válida"
        document.getElementById("from_error").style.visibility = "visible"
    }
    else {
        document.getElementById("from_error").style.visibility = "hidden"
    }

    to = new Date(document.getElementById("to_date").value);
    to_date = new Date(to.getFullYear(), to.getMonth(), to.getDate() + 1)

    if (from_date > to_date) {
        document.getElementById("interval_error").innerHTML = "Debe introducir un intervalo de tiempo válido"
        document.getElementById("interval_error").style.visibility = "visible"
    }
    else {
        document.getElementById("interval_error").style.visibility = "hidden"
    }
}

// Validación dinámica de la fecha final
function check_to_date() {
    to = new Date(document.getElementById("to_date").value);
    to_date = new Date(to.getFullYear(), to.getMonth(), to.getDate() + 1)
    today = new Date();

    if (to_date > today) {
        document.getElementById("to_error").innerHTML = "Debe introducir una fecha final válida"
        document.getElementById("to_error").style.visibility = "visible"
    }
    else {
        document.getElementById("to_error").style.visibility = "hidden"
    }

    from = new Date(document.getElementById("from_date").value);
    from_date = new Date(from.getFullYear(), from.getMonth(), from.getDate() + 1)

    if (from_date > to_date) {
        document.getElementById("interval_error").innerHTML = "Debe introducir un intervalo de tiempo válido"
        document.getElementById("interval_error").style.visibility = "visible"
    }
    else {
        document.getElementById("interval_error").style.visibility = "hidden"
    }
}

// Validación estática al momento de enviar el formulario
function validate() {
    error = false

    from = document.getElementById("from_date").value;
    to = document.getElementById("to_date").value;

    if (from == "") {
        document.getElementById("from_error").innerHTML = "Debe introducir una fecha inicial"
        document.getElementById("from_error").style.visibility = "visible"
    }
    else {
        document.getElementById("from_error").style.visibility = "hidden"
    }

    if (to == "") {
        document.getElementById("to_error").innerHTML = "Debe introducir una fecha final"
        document.getElementById("to_error").style.visibility = "visible"
    }
    else {
        document.getElementById("to_error").style.visibility = "hidden"
    }

    from_error = document.getElementById("from_error").style.visibility
    to_error = document.getElementById("to_error").style.visibility
    interval_error = document.getElementById("interval_error").style.visibility

    if (from_error == "visible" || to_error == "visible" || interval_error == "visible"){
        error = true
    }

    return (!error)
}
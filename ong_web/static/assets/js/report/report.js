/*
document.addEventListener('DOMContentLoaded', function() {
})
*/

document.getElementById("prueba").addEventListener("click", prueba)

function prueba() {
    
    from_date = document.getElementById("from_date").value.split("-")
    from_day = parseInt(from_date[2])
    from_month = parseInt(from_date[1])
    from_year = parseInt(from_date[0])

    to_date = document.getElementById("to_date").value.split("-")
    to_day = parseInt(to_date[2])
    to_month = parseInt(to_date[1])
    to_year = parseInt(to_date[0])

    today = new Date();
    day = parseInt(String(today.getDate()).padStart(2, '0'));
    month = parseInt(String(today.getMonth() + 1).padStart(2, '0'));
    year = today.getFullYear();

    
    console.log("from day: ", from_day)
    console.log("to day: ", to_day)
    console.log("day: ", day)
    console.log("from month: ", from_month)
    console.log("to month: ", to_month)
    console.log("month: ", month)
    console.log("from year: ", from_year)
    console.log("to year: ", to_year)
    console.log("year: ", year)
    
    // Validación del campo de fecha inicial
    if (from_year <= year) {
        if (from_month <= month) {
            if (from_day <= day) {
                document.getElementById("from_error").style.visibility = "hidden"
            }
            else {
                document.getElementById("from_error").innerHTML = "Debe introducir una fecha inicial válida"
                document.getElementById("from_error").style.visibility = "visible"
            }
        }
        else {
            document.getElementById("from_error").innerHTML = "Debe introducir una fecha inicial válida"
            document.getElementById("from_error").style.visibility = "visible"
        }
    }
    else {
        document.getElementById("from_error").innerHTML = "Debe introducir una fecha inicial válida"
        document.getElementById("from_error").style.visibility = "visible"
    }

    // Validación del campo de fecha final
    if (to_year <= year) {
        if (to_month <= month) {
            if (to_day <= day) {
                document.getElementById("to_error").style.visibility = "hidden"
            }
            else {
                document.getElementById("to_error").innerHTML = "Debe introducir una fecha final válida"
                document.getElementById("to_error").style.visibility = "visible"
            }
        }
        else {
            document.getElementById("to_error").innerHTML = "Debe introducir una fecha final válida"
            document.getElementById("to_error").style.visibility = "visible"
        }
    }
    else {
        document.getElementById("to_error").innerHTML = "Debe introducir una fecha final válida"
        document.getElementById("to_error").style.visibility = "visible"
    }

    // Validación del campo de fecha inicial con respecto al campo de fecha final
    if (from_year <= to_year) {
        if (from_month <= to_month) {
            if (from_day <= to_day) {
                document.getElementById("date_error").style.visibility = "hidden"
            }
            else {
                document.getElementById("date_error").innerHTML = "Debe introducir un intervalo de tiempo válido"
                document.getElementById("date_error").style.visibility = "visible"
            }
        }
        else {
            document.getElementById("date_error").innerHTML = "Debe introducir un intervalo de tiempo válido"
            document.getElementById("date_error").style.visibility = "visible"
        }
    }
    else {
        document.getElementById("date_error").innerHTML = "Debe introducir un intervalo de tiempo válido"
        document.getElementById("date_error").style.visibility = "visible"
    }






}

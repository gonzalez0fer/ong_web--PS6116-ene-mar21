document.addEventListener('DOMContentLoaded', function() {
    document.addEventListener("submit", validate)
})

function validate() {
    error = false

    operation_type = document.getElementById("operation_type").value
    water_liters = document.getElementById("water_liters").value
    water_amount = document.getElementById("water_amount"). value

    if (operation_type != "ingreso" && operation_type != "egreso") {
        document.getElementById("operation_type_error").innerHTML = "Debe seleccionar una opción válida"
        document.getElementById("operation_type_error").style.display = "block"
        error = true
    }

    if (water_liters < 1) {
        document.getElementById("water_liters_error").innerHTML = "Debe introducir una cantidad de litros mayor a 0"
        document.getElementById("water_liters_error").style.display = "block"
        error = true
    }

    if (water_amount < 0) {
        document.getElementById("water_amount_error").innerHTML = "Debe introducir un precio igual o mayor a 0"
        document.getElementById("water_amount_error").style.display = "block"
        error = true
    }

    if (operation_type == "ingreso") {
        if (tank_id.current_liters + water_liters > tank_id.capacity) {
            document.getElementById("water_liters_error").innerHTML = "Debe ingresar una cantidad válida para la capacidad del tanque"
            document.getElementById("water_liters_error").style.display = "block"
            error = true
        }
    }

    if (operation_type == "ingreso") {
        if (tank_id.current_liters < water_liters) {
            document.getElementById("water_liters_error").innerHTML = "No puede extraer más litros de la cantidad actual del tanque"
            document.getElementById("water_liters_error").style.display = "block"
            error = true
        }
    }

    if (error) {
        return false
    }

    else {
        return true
    }
}
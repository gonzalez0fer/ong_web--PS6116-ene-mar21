//document.addEventListener('DOMContentLoaded', function() {
//})

function validate() {
    error = false

    operation_type = document.getElementById("operation_type").value
    water_liters = document.getElementById("water_liters").value
    water_amount = document.getElementById("water_amount").value

    tank_capacity = parseInt(tank_capacity)
    tank_current_liters = parseInt(tank_current_liters)

    if (operation_type != "ingreso" && operation_type != "consumo") {
        document.getElementById("operation_type_error").innerHTML = "Debe seleccionar una opción"
        document.getElementById("operation_type_error").style.display = "block"
        error = true
    }
    else {
        document.getElementById("operation_type_error").style.display = "none"
    }

    if (water_liters == "") {
        document.getElementById("water_liters_error").innerHTML = "Debe introducir una cantidad de litros"
        document.getElementById("water_liters_error").style.display = "block"
        error = true
    }
    else if (parseInt(water_liters) < 1) {
        document.getElementById("water_liters_error").innerHTML = "Debe introducir una cantidad de litros mayor a 0"
        document.getElementById("water_liters_error").style.display = "block"
        error = true
    }
    else {
        document.getElementById("water_liters_error").style.display = "none"
    }

    if (water_amount == "") {
        document.getElementById("water_amount_error").innerHTML = "Debe introducir un precio"
        document.getElementById("water_amount_error").style.display = "block"
        error = true
    }
    else if (parseInt(water_amount) < 0) {
        document.getElementById("water_amount_error").innerHTML = "Debe introducir un precio igual o mayor a 0"
        document.getElementById("water_amount_error").style.display = "block"
        error = true
    }
    else {
        document.getElementById("water_amount_error").style.display = "none"
    }

    if (operation_type == "ingreso") {
        if (tank_current_liters + parseInt(water_liters) > tank_capacity) {
            document.getElementById("water_liters_error").innerHTML = "Debe ingresar una cantidad válida para la capacidad del tanque"
            document.getElementById("water_liters_error").style.display = "block"
            error = true
        }
    }

    if (operation_type == "consumo") {
        if (parseInt(water_liters) > tank_current_liters) {
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
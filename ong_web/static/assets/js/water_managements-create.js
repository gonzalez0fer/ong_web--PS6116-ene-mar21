document.addEventListener('DOMContentLoaded', function() {
    document.getElementById("operation_type").addEventListener("change", type_validation)
    document.getElementById("operation_description").addEventListener("change", description_validation)
    document.getElementById("water_liters").addEventListener("change", liters_validation)
    document.getElementById("water_amount").addEventListener("change", amount_validation)
})


function type_validation() {
    operation_type = document.getElementById("operation_type").value

    if (operation_type == "none") {
        document.getElementById("operation_type_error").innerHTML = "Debe seleccionar una opción válida"
        document.getElementById("operation_type_error").style.display = "block"
        error = true
    }
    else {
        document.getElementById("operation_type_error").style.display = "none"
    }
}


function description_validation() {
    operation_description = document.getElementById("operation_description").value

    if (operation_description == "none") {
        document.getElementById("operation_description_error").innerHTML = "Debe seleccionar una opción válida"
        document.getElementById("operation_description_error").style.display = "block"
        error = true
    }
    else {
        document.getElementById("operation_description_error").style.display = "none"
    }
}


function liters_validation() {
    water_liters = document.getElementById("water_liters").value

    if (parseInt(water_liters) < 1) {
        document.getElementById("water_liters_error").innerHTML = "Debe introducir una cantidad de litros mayor a 0"
        document.getElementById("water_liters_error").style.display = "block"
        error = true
    }
    else {
        document.getElementById("water_liters_error").style.display = "none"
    }

    operation_type = document.getElementById("operation_type").value
    tank_capacity = parseInt(tank_capacity)
    tank_current_liters = parseInt(tank_current_liters)

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
}


function amount_validation() {
    water_amount = document.getElementById("water_amount").value

    if (parseInt(water_amount) < 0) {
        document.getElementById("water_amount_error").innerHTML = "Debe introducir un precio igual o mayor a 0"
        document.getElementById("water_amount_error").style.display = "block"
        error = true
    }
    else {
        document.getElementById("water_amount_error").style.display = "none"
    }
}


function validate() {
    error = false

    operation_type = document.getElementById("operation_type").value
    operation_description = document.getElementById("operation_description").value
    water_liters = document.getElementById("water_liters").value
    water_amount = document.getElementById("water_amount").value

    if (operation_type == "none") {
        document.getElementById("operation_type_error").innerHTML = "Debe seleccionar una opción válida"
        document.getElementById("operation_type_error").style.display = "block"
        error = true
    }

    if (operation_description == "none") {
        document.getElementById("operation_description_error").innerHTML = "Debe seleccionar una opción válida"
        document.getElementById("operation_description_error").style.display = "block"
        error = true
    }

    if (water_liters == "") {
        document.getElementById("water_liters_error").innerHTML = "Debe introducir una cantidad de litros"
        document.getElementById("water_liters_error").style.display = "block"
        error = true
    }

    if (water_amount == "") {
        document.getElementById("water_amount_error").innerHTML = "Debe introducir un precio"
        document.getElementById("water_amount_error").style.display = "block"
        error = true
    }

    if (error) {
        return false
    }
    else {
        return true
    }
}
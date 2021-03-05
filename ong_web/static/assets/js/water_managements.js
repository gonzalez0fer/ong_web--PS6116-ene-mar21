document.addEventListener('DOMContentLoaded', function() {
    /* water_managements-create */
    document.getElementById("operation_type").addEventListener("change", type_validation)
    document.getElementById("operation_description").addEventListener("change", description_validation)

    if (window.location.href.includes("create")) {
        document.getElementById("water_liters").addEventListener("change", liters_validation)
    }
    
    document.getElementById("water_amount").addEventListener("change", amount_validation)

    /* water_managements-update */
    if (window.location.href.includes("update")) {
        document.getElementById("water_liters_update").addEventListener("change", liters_update_validation)
    }
})


function type_validation() {
    operation_type = document.getElementById("operation_type").value

    if (operation_type == "none") {
        document.getElementById("operation_type_error").innerHTML = "Debe seleccionar una opción válida"
        document.getElementById("operation_type_error").style.display = "block"
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
    }
    else {
        document.getElementById("water_liters_error").style.display = "none"
    }

    operation_type = document.getElementById("operation_type").value
    tank_capacity = parseInt(tank_capacity)
    tank_current_liters = parseInt(tank_current_liters)

    if (operation_type == "Ingreso") {
        if (tank_current_liters + parseInt(water_liters) > tank_capacity) {
            document.getElementById("water_liters_error").innerHTML = "Debe ingresar una cantidad válida para la capacidad del tanque"
            document.getElementById("water_liters_error").style.display = "block"
        }
    }

    if (operation_type == "Egreso") {
        if (parseInt(water_liters) > tank_current_liters) {
            document.getElementById("water_liters_error").innerHTML = "No puede extraer más litros de la cantidad actual del tanque"
            document.getElementById("water_liters_error").style.display = "block"
        }
    }
}


function amount_validation() {
    water_amount = document.getElementById("water_amount").value

    if (parseInt(water_amount) < 0) {
        document.getElementById("water_amount_error").innerHTML = "Debe introducir un precio igual o mayor a 0"
        document.getElementById("water_amount_error").style.display = "block"
    }
    else {
        document.getElementById("water_amount_error").style.display = "none"
    }
}


function validate() {
    error = false

    operation_type = document.getElementById("operation_type").value
    operation_description = document.getElementById("operation_description").value

    if (window.location.href.includes("create")) {
        water_liters = document.getElementById("water_liters").value
    }

    if (window.location.href.includes("update")) {
        water_liters = document.getElementById("water_liters_update").value
    }

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


function liters_update_validation() {
    water_liters = document.getElementById("water_liters_update").value
    
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
    original_quantity = parseInt(original_quantity)

    if (operation_type == "Ingreso") {
        if (tank_current_liters - original_quantity + parseInt(water_liters) > tank_capacity) {
            document.getElementById("water_liters_error").innerHTML = "Debe ingresar una cantidad válida para la capacidad del tanque"
            document.getElementById("water_liters_error").style.display = "block"
        }
    }

    if (operation_type == "Egreso") {
        if (parseInt(water_liters) > tank_current_liters) {
            document.getElementById("water_liters_error").innerHTML = "No puede extraer más litros de la cantidad actual del tanque"
            document.getElementById("water_liters_error").style.display = "block"
        }
    }
}
document.addEventListener('DOMContentLoaded', function() {
    
    document.getElementById("operation_type").addEventListener("change", type_validation)
    document.getElementById("operation_description").addEventListener("change", description_validation)
    document.getElementById("water_amount").addEventListener("change", amount_validation)
    
    // Solo para water_managements-create
    if (window.location.href.includes("create")) {
        document.getElementById("water_liters").addEventListener("change", liters_validation)
    }
    
    // Solo para water_managements-update
    if (window.location.href.includes("update")) {
        document.getElementById("operation_type").addEventListener("change", liters_update_validation)
        document.getElementById("water_liters").addEventListener("change", liters_update_validation)
    }
})

// Validación dinámica del tipo de operación
function type_validation() {
    operation_type = document.getElementById("operation_type").value

    // Si no es seleccionado un tipo de operación
    if (operation_type == "none") {
        document.getElementById("operation_type_error").innerHTML = "Debe seleccionar una opción válida"
        document.getElementById("operation_type_error").style.display = "block"
    }
    else {
        document.getElementById("operation_type_error").style.display = "none"
    }
}

// Validación dinámica de la descripción de la operación
function description_validation() {
    operation_description = document.getElementById("operation_description").value

    // Si no es seleccionada una  descripción
    if (operation_description == "none") {
        document.getElementById("operation_description_error").innerHTML = "Debe seleccionar una opción válida"
        document.getElementById("operation_description_error").style.display = "block"
    }
    else {
        document.getElementById("operation_description_error").style.display = "none"
    }
}

// Validación dinámica de la cantidad de litros
function liters_validation() {
    water_liters = document.getElementById("water_liters").value

    // Si la cantidad de litros introducida es menor a uno (1)
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

    // Si la operación es de tipo "ingreso"
    if (operation_type == "Ingreso") {

        // Si debido al ingreso se sobrepasa la capacidad máxima del tanque
        if (tank_current_liters + parseInt(water_liters) > tank_capacity) {
            document.getElementById("water_liters_error").innerHTML = "Debe ingresar una cantidad válida para la capacidad del tanque"
            document.getElementById("water_liters_error").style.display = "block"
        }
    }

    // Si la operación es de tipo "egreso"
    if (operation_type == "Egreso") {

        // Si se solicita egresar más cantidad de agua que la disponible
        if (parseInt(water_liters) > tank_current_liters) {
            document.getElementById("water_liters_error").innerHTML = "No puede extraer más litros de la cantidad actual del tanque"
            document.getElementById("water_liters_error").style.display = "block"
        }
    }
}

// Validación dinámica del monto del producto
function amount_validation() {
    water_amount = document.getElementById("water_amount").value

    // Si el monto introducido es menor o igual a cero (0)
    if (parseInt(water_amount) < 0) {
        document.getElementById("water_amount_error").innerHTML = "Debe introducir un precio igual o mayor a 0"
        document.getElementById("water_amount_error").style.display = "block"
    }
    else {
        document.getElementById("water_amount_error").style.display = "none"
    }
}

// Validación estática al momento de enviar el formulario
function validate() {
    error = false

    operation_type = document.getElementById("operation_type").value
    operation_description = document.getElementById("operation_description").value
    water_liters = document.getElementById("water_liters").value
    water_amount = document.getElementById("water_amount").value

    // Si no es seleccionado un tipo de operación
    if (operation_type == "none") {
        document.getElementById("operation_type_error").innerHTML = "Debe seleccionar una opción válida"
        document.getElementById("operation_type_error").style.display = "block"
        error = true
    }

    // Si no es seleccionada una descripción
    if (operation_description == "none") {
        document.getElementById("operation_description_error").innerHTML = "Debe seleccionar una opción válida"
        document.getElementById("operation_description_error").style.display = "block"
        error = true
    }

    // Si no se introduce una cantidad de litros
    if (water_liters == "") {
        document.getElementById("water_liters_error").innerHTML = "Debe introducir una cantidad de litros"
        document.getElementById("water_liters_error").style.display = "block"
        error = true
    }

    // Si no se introduce un monto
    if (water_amount == "") {
        document.getElementById("water_amount_error").innerHTML = "Debe introducir un precio"
        document.getElementById("water_amount_error").style.display = "block"
        error = true
    }

    operation_type_error = document.getElementById("operation_type_error").style.display
    operation_description_error = document.getElementById("operation_description_error").style.display
    water_liters_error = document.getElementById("water_liters_error").style.display
    water_amount_error = document.getElementById("water_amount_error").style.display

    if (operation_type_error == "block" || operation_description_error == "block" || water_liters_error == "block" || water_amount_error == "block"){
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

// Validación dinámica de la actualización de litros
function liters_update_validation() {
    operation_type_update = document.getElementById("operation_type").value
    water_liters_update = parseInt(document.getElementById("water_liters").value)

    // Si la cantidad de litros para la operación es menor a uno (1)
    if (water_liters_update < 1) {
        document.getElementById("water_liters_error").innerHTML = "Debe introducir una cantidad de litros mayor a 0"
        document.getElementById("water_liters_error").style.display = "block"
    }
    else {
        document.getElementById("water_liters_error").style.display = "none"
    }

    tank_capacity = parseInt(tank_capacity)
    current_tank_liters = parseInt(current_tank_liters)
    original_operation_liters = parseInt(original_operation_liters)
    original_operation_type = original_operation_type
    
    var base_quantity

    // Dependiendo del tipo de operación, se hace una regresión acorde para tener la cantidad de litros disponibles
    if (original_operation_type == "Ingreso") {
        base_quantity = current_tank_liters - original_operation_liters    
    }
    else {
        base_quantity = current_tank_liters + original_operation_liters
    }

    console.log("base: ", base_quantity)

    // Si el nuevo tipo de operación es "ingreso"
    if (operation_type_update == "Ingreso") {

        // Si, debido a la nueva cantidad ingresada, se sobrepasa la capacidad máxima del tanque
        if (base_quantity + water_liters_update > tank_capacity) {
            document.getElementById("water_liters_error").innerHTML = "Debe ingresar una cantidad válida para la capacidad del tanque"
            document.getElementById("water_liters_error").style.display = "block"
        }

        // Si, debido a la nueva cantidad ingreada, la cantidad del tanque es menor a cero (0)
        if (base_quantity + water_liters_update < 0) {
            document.getElementById("water_liters_error").innerHTML = "Operación inválida"
            document.getElementById("water_liters_error").style.display = "block"
        }
    }
    // Si el nuevo tipo de operación es "egreso"
    else {

        // Si, debido a la nueva cantidad egresada, la cantidad del tanque es menor a cero (0) 
        if (base_quantity - water_liters_update < 0) {
            document.getElementById("water_liters_error").innerHTML = "No puede extraer más litros de la cantidad actual del tanque"
            document.getElementById("water_liters_error").style.display = "block"
        }

        // Si, debido a la nueva cantidad egresada, se sobrepasa la capacidad máxima del tanque
        if (base_quantity - water_liters_update > tank_capacity) {
            console.log("sfgsdfug")
            document.getElementById("water_liters_error").innerHTML = "Operación inválida"
            document.getElementById("water_liters_error").style.display = "block"
        }
    }
}
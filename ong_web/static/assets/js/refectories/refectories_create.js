document.addEventListener('DOMContentLoaded', function() {
    document.getElementById("name").addEventListener("change", name_validation)
    document.getElementById("water_price").addEventListener("change", water_price_validation)
    document.getElementById("capacity").addEventListener("change", capacity_validation)
    document.getElementById("current_liters").addEventListener("change", current_liters_validation)
    document.getElementById("address").addEventListener("change", address_validation)
})

// Validación dinámica de nombre del punto de distribución
function name_validation() {
    ref_name = document.getElementById("name").value;

    if (ref_name == "" || ref_name == "none") {
        document.getElementById("name_error").innerHTML = "Introduzca nombre del punto de Distribución"
        document.getElementById("name_error").style.visibility = "visible"
    }
    else {
        document.getElementById("name_error").style.visibility = "hidden"
    }
}

// Validación dinámica del precio del agua.
function water_price_validation() {
    water_price = document.getElementById("water_price").value;

    if (water_price == "" || water_price == "none") {
        document.getElementById("water_price_error").innerHTML = "Introduzca el precio del agua"
        document.getElementById("water_price_error").style.visibility = "visible"
    }
    else if (parseFloat(water_price) < 0) {
        document.getElementById("water_price_error").innerHTML = "Precio del agua inválido. Debe ser mayor a 0"
        document.getElementById("water_price_error").style.visibility = "visible"
    }
    else {
        document.getElementById("water_price_error").style.visibility = "hidden"
    }
}

// Validación dinámica de la capacidad del tanque
function capacity_validation() {
    capacity = document.getElementById("capacity").value;

    if (capacity == "" || capacity == "none") {
        document.getElementById("capacity_error").innerHTML = "Introduzca la capacidad del tanque de agua"
        document.getElementById("capacity_error").style.visibility = "visible"
    }
    else if (parseFloat(capacity) % 1 != 0 || parseFloat(capacity) < 1) {
        document.getElementById("capacity_error").innerHTML = "Cantidad inválida. Use números enteros y mayores a 0"
        document.getElementById("capacity_error").style.visibility = "visible"
    }
    else {
        document.getElementById("capacity_error").style.visibility = "hidden"
    }
}

// Validación dinámica de la cantidad de agua actual en el tanque
function current_liters_validation() {
    current_liters = document.getElementById("current_liters").value;

    if (current_liters == "" || current_liters == "none") {
        document.getElementById("current_liters_error").innerHTML = "Introduzca cantidad de litros actuales del tanque de agua"
        document.getElementById("current_liters_error").style.visibility = "visible"
    }
    else if (parseFloat(current_liters) % 1 != 0 || parseFloat(current_liters) < 1) {
        document.getElementById("current_liters_error").innerHTML = "Cantidad inválida. Use números enteros y mayores a 0"
        document.getElementById("current_liters_error").style.visibility = "visible"
    }
    else {
        document.getElementById("current_liters_error").style.visibility = "hidden"
    }
}

// Validación dinámica de la dirección del Punto de distribución
function address_validation() {
    address = document.getElementById("address").value;

    if (address == "" || address == "none") {
        document.getElementById("address_error").innerHTML = "Introduzca la dirección del punto de distribución"
        document.getElementById("address_error").style.visibility = "visible"
    }
    else {
        document.getElementById("address_error").style.visibility = "hidden"
    }
}

// ----------- Validación estática ---------- //
function validate() {
    error = false

    // Getting every form field. (Model field also)
    ref_name = document.getElementById("name").value;
    water_price = document.getElementById("water_price").value;
    capacity = document.getElementById("capacity").value;
    current_liters = document.getElementById("current_liters").value;
    address = document.getElementById("address").value; 
    description = document.getElementById("description").value; 

    // Validación del nombre del punto de distribución
    if (ref_name == "" || ref_name == "none") {
        document.getElementById("name_error").innerHTML = "Introduzca nombre del punto de Distribución"
        document.getElementById("name_error").style.visibility = "visible"
        error = true
    }
    else {
        document.getElementById("name_error").style.visibility = "hidden"
    }

    // Validación del precio del agua
    if (water_price == "" || water_price == "none") {
        document.getElementById("water_price_error").innerHTML = "Introduzca el precio del agua"
        document.getElementById("water_price_error").style.visibility = "visible"
        error = true
    }
    else if (parseFloat(water_price) < 0) {
        document.getElementById("water_price_error").innerHTML = "Precio del agua inválido. Debe ser mayor a 0"
        document.getElementById("water_price_error").style.visibility = "visible"
        error = true
    }
    else {
        document.getElementById("water_price_error").style.visibility = "hidden"
    }

    // Validación de la capacidad del tanque
    if (capacity == "" || capacity =="none") {
        document.getElementById("capacity_error").innerHTML = "Introduzca la capacidad del tanque de agua"
        document.getElementById("capacity_error").style.visibility = "visible"
        error = true
    }
    else if (parseFloat(capacity) % 1 != 0 || parseFloat(capacity) < 1) {
        document.getElementById("capacity_error").innerHTML = "Cantidad inválida. Use números enteros y mayores a 0"
        document.getElementById("capacity_error").style.visibility = "visible"
        error = true
    }
    else {
        document.getElementById("capacity_error").style.visibility = "hidden"
    }

    // Validación de los litros actuales en el tanque
    if (current_liters == "" || current_liters =="none") {
        document.getElementById("current_liters_error").innerHTML = "Introduzca la cantidad de litros de agua en el tanque actualmente."
        document.getElementById("current_liters_error").style.visibility = "visible"
        error = true
    }
    else if (parseFloat(current_liters) % 1 != 0 || parseFloat(current_liters) < 1) {
        document.getElementById("current_liters_error").innerHTML = "Cantidad inválida. Use números enteros y mayores a 0"
        document.getElementById("current_liters_error").style.visibility = "visible"
        error = true
    }
    else if (parseFloat(current_liters) > parseFloat(capacity)) {
        document.getElementById("current_liters_error").innerHTML = "La cantidad es mayor a la capacidad del tanque"
        document.getElementById("current_liters_error").style.visibility = "visible"
        error = true
    }
    else {
        document.getElementById("current_liters_error").style.visibility = "hidden"
    }

    // Validación de la dirección del punto de distribución
    if (address == "none" || address == "") {
        document.getElementById("address_error").innerHTML = "Introduzca la dirección del punto de distribución"
        document.getElementById("address_error").style.visibility = "visible"
        error = true
    }
    else {
        document.getElementById("address_error").style.visibility = "hidden"
    }

    return !error
}
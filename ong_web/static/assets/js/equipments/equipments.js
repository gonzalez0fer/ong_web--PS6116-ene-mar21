document.addEventListener('DOMContentLoaded', function() {
    // Verificación dinámica de campos (Create & Update)
    document.getElementById("name").addEventListener("change", name_validation)
    document.getElementById("maintenance_frequency").addEventListener("change", maintenance_frequency_validation)    
    document.getElementById("brand").addEventListener("change", brand_validation)    
    document.getElementById("power").addEventListener("change", power_validation)
    document.getElementById("inlet_diameter").addEventListener("change", inlet_diameter_validation)    
    document.getElementById("diameter").addEventListener("change", diameter_validation)    
    document.getElementById("height").addEventListener("change", height_validation)
    document.getElementById("volume").addEventListener("change", volume_validation) 
    document.getElementById("flow").addEventListener("change", flow_validation)    
    document.getElementById("light_bulb_size").addEventListener("change", light_bulb_size_validation)
    document.getElementById("quartz_size").addEventListener("change", quartz_size_validation)
})

// Validación dinámica del nombre del equipo
function name_validation() {
    eq_name = document.getElementById("name").value;

    if (eq_name == "none" || eq_name == "") {
        document.getElementById("name_error").innerHTML = "Introduzca nombre del equipo"
        document.getElementById("name_error").style.visibility = "visible"
    }
    else {
        document.getElementById("name_error").style.visibility = "hidden"
    }
}

// Validación dinámica de la frecuencia de mantenimiento del equippo
function maintenance_frequency_validation() {
    maintenance_frequency = document.getElementById("maintenance_frequency").value;

    if (maintenance_frequency == "none" || maintenance_frequency == "") {
        document.getElementById("maintenance_frequency_error").innerHTML = "Elija la frecuencia de mantenimiento del equipo"
        document.getElementById("maintenance_frequency_error").style.visibility = "visible"
    }
    else {
        document.getElementById("maintenance_frequency_error").style.visibility = "hidden"
    }
}

// Validación dinámica de la marca del equipo
function brand_validation() {
    brand = document.getElementById("brand").value;

    if (brand == "none" || brand == "") {
        document.getElementById("brand_error").innerHTML = "Introduzca la marca del equipo"
        document.getElementById("brand_error").style.visibility = "visible"
    }
    else {
        document.getElementById("brand_error").style.visibility = "hidden"
    }
}

// Validación dinámica de la potencia del equipo
function power_validation() {
    power = document.getElementById("power").value; 

    if (power != "none" && power != "" && parseFloat(power) < 1) {
        document.getElementById("power_error").innerHTML = "Cantidad inválida"
        document.getElementById("power_error").style.visibility = "visible"
    }
    else {
        document.getElementById("power_error").style.visibility = "hidden"
    }
}

// validación del diámetro interno del equipo
function inlet_diameter_validation() {
    inlet_diameter = document.getElementById("inlet_diameter").value;

    if (inlet_diameter != "none" && inlet_diameter != "" && parseFloat(inlet_diameter) < 1) {
        document.getElementById("inlet_diameter_error").innerHTML = "Cantidad inválida"
        document.getElementById("inlet_diameter_error").style.visibility = "visible"
    }
    else {
        document.getElementById("inlet_diameter_error").style.visibility = "hidden"
    }
}

function diameter_validation () {
    diameter = document.getElementById("diameter").value; // Validacion de negativos

    if (diameter != "none" && diameter != "" && parseFloat(diameter) < 1) {
        document.getElementById("diameter_error").innerHTML = "Cantidad inválida"
        document.getElementById("diameter_error").style.visibility = "visible"
    }
    else {
        document.getElementById("diameter_error").style.visibility = "hidden"
    }
}

function height_validation(){
    height = document.getElementById("height").value; // Validacion de negativos

    if (height != "none" && height != "" && parseFloat(height) < 1) {
        document.getElementById("height_error").innerHTML = "Cantidad inválida"
        document.getElementById("height_error").style.visibility = "visible"
    }
    else {
        document.getElementById("height_error").style.visibility = "hidden"
    }
}

function volume_validation() {
    volume = document.getElementById("volume").value;

    if (volume != "none" && volume != "" && parseFloat(volume) < 1) {
        document.getElementById("volume_error").innerHTML = "Cantidad inválida"
        document.getElementById("volume_error").style.visibility = "visible"
    }
    else {
        document.getElementById("volume_error").style.visibility = "hidden"
    }
}

function flow_validation() {
    flow = document.getElementById("flow").value;

    if (flow != "none" && flow != "" && parseFloat(flow) < 1) {
        document.getElementById("flow_error").innerHTML = "Cantidad inválida"
        document.getElementById("flow_error").style.visibility = "visible"
    }
    else {
        document.getElementById("flow_error").style.visibility = "hidden"
    }
}

function light_bulb_size_validation() {
    light_bulb_size = document.getElementById("light_bulb_size").value; 

    if (light_bulb_size != "none" && light_bulb_size != "" && parseFloat(light_bulb_size) < 1) {
        document.getElementById("light_bulb_size_error").innerHTML = "Tamaño inválido"
        document.getElementById("light_bulb_size_error").style.visibility = "visible"
    }
    else {
        document.getElementById("light_bulb_size_error").style.visibility = "hidden"
    }
}

function quartz_size_validation() {
    quartz_size = document.getElementById("quartz_size").value; 

    if (quartz_size != "none" && quartz_size != "" && parseFloat(quartz_size) < 1) {
        document.getElementById("quartz_size_error").innerHTML = "Tamaño inválido"
        document.getElementById("quartz_size_error").style.visibility = "visible"
    }
    else {
        document.getElementById("quartz_size_error").style.visibility = "hidden"
    }
}


// Función de validación del form
function validate() {
    
    error = false

    // Getting every form field. (Model field also)
    eq_name = document.getElementById("name").value;
    maintenance_frequency = document.getElementById("maintenance_frequency").value;
    brand = document.getElementById("brand").value;
    equipment_model = document.getElementById("equipment_model").value;
    power = document.getElementById("power").value; // Validacion de negativos
    inlet_diameter = document.getElementById("inlet_diameter").value; // Validacion de negativos
    diameter = document.getElementById("diameter").value; // Validacion de negativos
    height = document.getElementById("height").value; // Validacion de negativos
    volume = document.getElementById("volume").value; // Validacion de negativos
    measurements = document.getElementById("measurements").value; 
    flow = document.getElementById("flow").value; // Validacion de negativos
    light_bulb_size = document.getElementById("light_bulb_size").value; // Validacion de negativos
    quartz_size = document.getElementById("quartz_size").value; // Validacion de negativos

    // Validación del nombre del equipo
    if (eq_name == "" || eq_name == "none") {
        document.getElementById("name_error").innerHTML = "Introduzca nombre del equipo"
        document.getElementById("name_error").style.visibility = "visible"
        error = true
    }
    else {
        document.getElementById("name_error").style.visibility = "hidden"
    }

    // Validación de la frecuencia del mantenimiento del equipo
    if (maintenance_frequency == "" || maintenance_frequency == "none") {
        document.getElementById("maintenance_frequency_error").innerHTML = "Elija la frecuencia de mantenimiento del equipo"
        document.getElementById("maintenance_frequency_error").style.visibility = "visible"
        error = true
    }
    else {
        document.getElementById("maintenance_frequency_error").style.visibility = "hidden"
    }

    // Validación de la marca del equipo
    if (brand == "" || brand =="none") {
        document.getElementById("brand_error").innerHTML = "Introduzca marca del equipo"
        document.getElementById("brand_error").style.visibility = "visible"
        error = true
    }
    else {
        document.getElementById("brand_error").style.visibility = "hidden"
    }

    // Verificar la potencia
    if (power != "none" && power != "" && parseFloat(power) < 1) {
        document.getElementById("power_error").innerHTML = "Cantidad inválida"
        document.getElementById("power_error").style.visibility = "visible"
        error = true
    }
    else {
        document.getElementById("power_error").style.visibility = "hidden"
    }

    // Verificar el diámetro interno
    if (inlet_diameter != "none" && inlet_diameter != "" && parseFloat(inlet_diameter) < 1) {
        document.getElementById("inlet_diameter_error").innerHTML = "Cantidad inválida"
        document.getElementById("inlet_diameter_error").style.visibility = "visible"
        error = true
    }
    else {
        document.getElementById("inlet_diameter_error").style.visibility = "hidden"
    }

    // Verificar el diámetro
    if (diameter != "none" && diameter != "" && parseFloat(diameter) < 1) {
        document.getElementById("diameter_error").innerHTML = "Cantidad inválida"
        document.getElementById("diameter_error").style.visibility = "visible"
        error = true
    }
    else {
        document.getElementById("diameter_error").style.visibility = "hidden"
    }

    // Verificar la altura
    if (height != "none" && height != "" && parseFloat(height) < 1) {
        document.getElementById("height_error").innerHTML = "Cantidad inválida"
        document.getElementById("height_error").style.visibility = "visible"
        error = true
    }
    else {
        document.getElementById("height_error").style.visibility = "hidden"
    }

    // Verificar el volumen
    if (volume != "none" && volume != "" && parseFloat(volume) < 1) {
        document.getElementById("volume_error").innerHTML = "Cantidad inválida"
        document.getElementById("volume_error").style.visibility = "visible"
        error = true
    }
    else {
        document.getElementById("volume_error").style.visibility = "hidden"
    }

    // Verificar el flujo
    if (flow != "none" && flow != "" && parseFloat(flow) < 1) {
        document.getElementById("flow_error").innerHTML = "Cantidad inválida"
        document.getElementById("flow_error").style.visibility = "visible"
        error = true
    }
    else {
        document.getElementById("flow_error").style.visibility = "hidden"
    }

    // Verificar tamaño del bombillo
    if (light_bulb_size != "none" && light_bulb_size != "" && parseFloat(light_bulb_size) < 1) {
        document.getElementById("light_bulb_size_error").innerHTML = "Tamaño inválido"
        document.getElementById("light_bulb_size_error").style.visibility = "visible"
        error = true
    }
    else {
        document.getElementById("light_bulb_size_error").style.visibility = "hidden"
    }

    // Verificar tamaño del cuarzo
    if (quartz_size != "none" && quartz_size != "" && parseFloat(quartz_size) < 1) {
        document.getElementById("quartz_size_error").innerHTML = "Tamaño inválido"
        document.getElementById("quartz_size_error").style.visibility = "visible"
        error = true
    }
    else {
        document.getElementById("quartz_size_error").style.visibility = "hidden"
    }


    return !error
}
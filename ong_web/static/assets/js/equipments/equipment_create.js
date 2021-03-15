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
        document.getElementById("name_error").style.display = "block"
        error = true
    }
    else {
        document.getElementById("name_error").style.display = "none"
    }

    // Validación de la frecuencia del mantenimiento del equipo
    if (maintenance_frequency == "" || maintenance_frequency == "none") {
        document.getElementById("maintenance_frequency_error").innerHTML = "Introduzca la frecuencia del mantenimiento"
        document.getElementById("maintenance_frequency_error").style.display = "block"
        error = true
    }
    else {
        document.getElementById("maintenance_frequency_error").style.display = "none"
    }

    // Validación de la marca del equipo
    if (brand == "" || brand =="none") {
        document.getElementById("brand_error").innerHTML = "Introduzca marca del equipo"
        document.getElementById("brand_error").style.display = "block"
        error = true
    }
    else {
        document.getElementById("brand_error").style.display = "none"
    }

    // Verificar el modelo del equipo
    // if (equipment_model == "") {
    //     document.getElementById("equipment_model_error").innerHTML = "Introduzca modelo del equipo"
    //     document.getElementById("equipment_model_error").style.display = "block"
    //     error = true
    // }
    // else {
    //     document.getElementById("equipment_model_error").style.display = "none"
    // }

    // Verificar la potencia
    if (power != "none" && power != "" && parseFloat(power) < 1) {
        document.getElementById("power_error").innerHTML = "Cantidad inválida"
        document.getElementById("power_error").style.display = "block"
        error = true
    }
    else {
        document.getElementById("power_error").style.display = "none"
    }

    // Verificar el diámetro interno
    if (inlet_diameter != "none" && inlet_diameter != "" && parseFloat(inlet_diameter) < 1) {
        document.getElementById("inlet_diameter_error").innerHTML = "Cantidad inválida"
        document.getElementById("inlet_diameter_error").style.display = "block"
        error = true
    }
    else {
        document.getElementById("inlet_diameter_error").style.display = "none"
    }

    // Verificar el diámetro
    if (diameter != "none" && diameter != "" && parseFloat(diameter) < 1) {
        document.getElementById("diameter_error").innerHTML = "Cantidad inválida"
        document.getElementById("diameter_error").style.display = "block"
        error = true
    }
    else {
        document.getElementById("diameter_error").style.display = "none"
    }

    // Verificar la altura
    if (height != "none" && height != "" && parseFloat(height) < 1) {
        document.getElementById("height_error").innerHTML = "Cantidad inválida"
        document.getElementById("height_error").style.display = "block"
        error = true
    }
    else {
        document.getElementById("height_error").style.display = "none"
    }

    // Verificar el volumen
    if (volume != "none" && volume != "" && parseFloat(volume) < 1) {
        document.getElementById("volume_error").innerHTML = "Cantidad inválida"
        document.getElementById("volume_error").style.display = "block"
        error = true
    }
    else {
        document.getElementById("volume_error").style.display = "none"
    }

    // Verificar el flujo
    if (flow != "none" && flow != "" && parseFloat(flow) < 1) {
        document.getElementById("flow_error").innerHTML = "Cantidad inválida"
        document.getElementById("flow_error").style.display = "block"
        error = true
    }
    else {
        document.getElementById("flow_error").style.display = "none"
    }

    // Verificar tamaño del bombillo
    if (light_bulb_size != "none" && light_bulb_size != "" && parseFloat(light_bulb_size) < 1) {
        document.getElementById("light_bulb_size_error").innerHTML = "Tamaño inválido"
        document.getElementById("light_bulb_size_error").style.display = "block"
        error = true
    }
    else {
        document.getElementById("light_bulb_size_error").style.display = "none"
    }

    // Verificar tamaño del cuarzo
    if (quartz_size != "none" && quartz_size != "" && parseFloat(quartz_size) < 1) {
        document.getElementById("quartz_size_error").innerHTML = "Tamaño inválido"
        document.getElementById("quartz_size_error").style.display = "block"
        error = true
    }
    else {
        document.getElementById("quartz_size_error").style.display = "none"
    }


    return !error
}
function validate() {
    error = false

    // Getting every form field. (Model field also)
    eq_name = document.getElementById("name").value;
    maintenance_frequency = document.getElementById("maintenance_frequency").value;
    brand = document.getElementById("brand").value;
    equipment_model = document.getElementById("equipment_model").value;
    power = document.getElementById("power").value;
    brand = document.getElementById("brand").value;
    inlet_diameter = document.getElementById("inlet_diameter").value;
    diameter = document.getElementById("diameter").value;
    height = document.getElementById("height").value;
    volume = document.getElementById("volume").value;
    measurements = document.getElementById("measurements").value;
    flow = document.getElementById("flow").value;
    light_bulb_size = document.getElementById("light_bulb_size").value;
    quartz_size = document.getElementById("quartz_size").value;

    // Validación del nombre del equipo
    if (eq_name == "") {
        document.getElementById("name_error").innerHTML = "Introduzca nombre del equipo"
        document.getElementById("name_error").style.display = "block"
        error = true
    }
    else {
        document.getElementById("name_error").style.display = "none"
    }

    if (operation_type != "Ingreso" && operation_type != "Egreso") {
        document.getElementById("operation_type_error").innerHTML = "Debe seleccionar una opción"
        document.getElementById("operation_type_error").style.display = "block"
        error = true
    }
    else {
        document.getElementById("operation_type_error").style.display = "none"
    }

    console.log(product_quantity)
    // Verificar que la cantidad del producto sea valida
    if (product_quantity == "") {
        document.getElementById("product_quantity_error").innerHTML = "Debe introducir una cantidad válida"
        document.getElementById("product_quantity_error").style.display = "block"
        error = true
    }
    else if (parseInt(product_quantity) <= 0) {
        document.getElementById("product_quantity_error").innerHTML = "Debe introducir una cantidad mayor a 0"
        document.getElementById("product_quantity_error").style.display = "block"
        error = true
    }
    else {
        document.getElementById("product_quantity_error").style.display = "none"
    }

    // Verificar que el precio del producto sea valida
    if (product_unitary_amount == "") {
        document.getElementById("product_unitary_amount_error").innerHTML = "Debe introducir una cantidad válida"
        document.getElementById("product_unitary_amount_error").style.display = "block"
        error = true
    }
    else if (parseFloat(product_unitary_amount) < 0) {
        document.getElementById("product_unitary_amount_error").innerHTML = "Debe introducir precio mayor o igual a 0"
        document.getElementById("product_unitary_amount_error").style.display = "block"
        error = true
    }
    else {
        document.getElementById("product_unitary_amount_error").style.display = "none"
    }

    // Verificar que, si la operacion es de Egreso...
    if (operation_type == "Egreso") {
        const found = products.find(product => product.product_name == product_cod);

        // ... Existe el producto a consumir...
        if (!found) {
            document.getElementById("operation_type_error").innerHTML = "El producto seleccionado no se pudo encontrar"
            document.getElementById("operation_type_error").style.display = "block"
            error = true
        } else {
            // ... Si existe, que la cantidad pedida no exceda la cantidad disponible
            if (parseInt(product_quantity) > parseInt(found.product_quantity)) {
                document.getElementById("product_quantity_error").innerHTML = "La cantidad pedida excede la cantidad disponible"
                document.getElementById("product_quantity_error").style.display = "block"
                error = true
            } else {
                document.getElementById("operation_type_error").style.display = "none"
            }
        }
    }

    return !error
}
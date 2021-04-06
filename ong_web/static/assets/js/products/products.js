document.addEventListener('DOMContentLoaded', function() {
    
    document.getElementById("product_unitary_amount").addEventListener("change", amount_validation)
    document.getElementById("product_unit").addEventListener("change", unit_validation)
    
    // Solo para product_create
    if (window.location.href.includes("create")) {
        document.getElementById("product_cod").addEventListener("change", cod_validation)
        document.getElementById("product_cod").addEventListener("change", quantity_validation)
        document.getElementById("product_cod").addEventListener("change", amount_validation)
        document.getElementById("product_cod").addEventListener("change", unit_validation)
        document.getElementById("product_cod").addEventListener("change", spare_part_validation)
        document.getElementById("product_quantity").addEventListener("change", quantity_validation)
    }

    // Solo para cupboard_management_update
    if (window.location.href.includes("update")) {
        document.getElementById("operation_type").addEventListener("change", quantity_update_validation)
        document.getElementById("product_quantity").addEventListener("change", quantity_update_validation)
    }
})

var unit_found = false;

// Validación dinámica del nombre del producto
function cod_validation() {
    product_cod = document.getElementById("product_cod").value
    operation_type = document.getElementById("operation_type").value

    // Si es introducido un nombre
    if (product_cod != "" && product_cod != "none") {
        // Si la operación es un "egreso", verifico si el producto introducido existe
        if (operation_type == "Egreso") {
            found = products.find(product => product.product_name == product_cod);

            if (!found) {
                document.getElementById("product_cod_error").innerHTML = "El producto seleccionado no se encuentra registrado"
                document.getElementById("product_cod_error").style.visibility = "visible"
            }
            else {
                document.getElementById("product_cod_error").style.visibility = "hidden"
            }
        } else {
            document.getElementById("product_cod_error").style.visibility = "hidden"
        } 
    } else {
        document.getElementById("product_cod_error").innerHTML = "Debe introducir el nombre del producto"
        document.getElementById("product_cod_error").style.visibility = "visible"
    }
}

// Validación dinámica de la cantidad del producto
function quantity_validation() {
    product_quantity = parseFloat(document.getElementById("product_quantity").value)
    operation_type = document.getElementById("operation_type").value

    // Si la cantidad del producto introducida es menor a uno (1)
    if (product_quantity < 1) {
        document.getElementById("product_quantity_error").innerHTML = "Debe introducir una cantidad mayor a 0"
        document.getElementById("product_quantity_error").style.visibility = "visible"
        return
    }

    // Si la cantidad del producto introducida es mayor o igual a uno (1)
    else if (product_quantity >= 1) {

        // Si la cantidad del producto introducida posee decimales o es mayor a la capacidad de la BD
        if (product_quantity % 1 != 0 || product_quantity > 2147483647) {
            document.getElementById("product_quantity_error").innerHTML = "Debe introducir una cantidad válida"
            document.getElementById("product_quantity_error").style.visibility = "visible"
            return
        }
        else {
            document.getElementById("product_quantity_error").style.visibility = "hidden"
        }
    }
    else {
        document.getElementById("product_quantity_error").style.visibility = "hidden"
    }

    // Si la operación es un "egreso", verifico la cantidad disponible del producto
    if (operation_type == "Egreso") {
        found = products.find(product => product.product_name == product_cod);

        if (found) {
            if (product_quantity > parseInt(found.product_quantity)) {
                document.getElementById("product_quantity_error").innerHTML = "La cantidad pedida excede la cantidad disponible"
                document.getElementById("product_quantity_error").style.visibility = "visible"
            }
            else {
                document.getElementById("product_quantity_error").style.visibility = "hidden"
            }
        }
    }
}

// Validación dinámica del monto del producto
function amount_validation() {
    product_unitary_amount = parseFloat(document.getElementById("product_unitary_amount").value)

    // Si el monto introducido es menor a cero (0)
    if (product_unitary_amount < 0) {
        document.getElementById("product_unitary_amount_error").innerHTML = "Debe introducir un precio igual o mayor a 0"
        document.getElementById("product_unitary_amount_error").style.visibility = "visible"
    }
    else {
        document.getElementById("product_unitary_amount_error").style.visibility = "hidden"
    }
}

// Validacion dinámica de las unidades del producto
function unit_validation() {

    product_cod = document.getElementById("product_cod").value;
    const found = products.find(product => product.product_name == product_cod);

    if (found) {
        document.getElementById("product_unit").value = found.product_unit;
        document.getElementById("product_unit").setAttribute("disabled", 'disabled');
        document.getElementById("product_unit_error").style.visibility = "hidden"
        unit_found = true;
    } else if (!found && document.getElementById("product_unit").disabled) {
        document.getElementById("product_unit").disabled = false;
        document.getElementById("product_unit_error").style.visibility = "hidden"
        unit_found = false;
    } else {
        document.getElementById("product_unit_error").style.visibility = "hidden"
    }

}

// Validacion dinámica de las unidades del producto
function spare_part_validation() {

    product_cod = document.getElementById("product_cod").value;
    const found = products.find(product => product.product_name == product_cod);

    if (found) {
        if (found.is_spare_part == "False") {
            document.getElementById("is_spare_part").checked = false;
        } else {
            document.getElementById("is_spare_part").checked = true;
        }
        document.getElementById("is_spare_part").setAttribute("disabled", 'disabled');
        unit_found = true;
    } else if (!found && document.getElementById("is_spare_part").disabled) {
        document.getElementById("is_spare_part").disabled = false;
        document.getElementById("is_spare_part").checked = false;
        unit_found = false;
    } else {
        document.getElementById("is_spare_part_error").style.visibility = "hidden"
    }

}


// Validación estática al momento de enviar el formulario
function validate() {

    error = false

    // Solo para product_management_create 
    if (window.location.href.includes("create")) {
        product_name = document.getElementById("product_cod").value
    } else if (window.location.href.includes("update")) {
        product_name = document.getElementById("product_name").value
    }

    product_unit = document.getElementById("product_unit").value
    product_quantity = document.getElementById("product_quantity").value
    product_unitary_amount = document.getElementById("product_unitary_amount").value

    if (document.getElementById("product_unit").disabled) {
        document.getElementById("product_unit").disabled = false;
        document.getElementById("is_spare_part").disabled = false;
    }

    // Si el nombre del producto es vacío
    if (product_name == "") {
        document.getElementById("product_cod_error").innerHTML = "Debe introducir el nombre del producto"
        document.getElementById("product_cod_error").style.visibility = "visible"
        error = true
    } 

    // Si la cantidad del producto es vacía
    if (product_quantity == "") {
        document.getElementById("product_quantity_error").innerHTML = "Debe introducir una cantidad mayor a 0"
        document.getElementById("product_quantity_error").style.visibility = "visible"
        error = true
    }

    // Si el monto del producto es vacío
    if (product_unitary_amount == "") {
        document.getElementById("product_unitary_amount_error").innerHTML = "Debe introducir un precio igual o mayor a 0"
        document.getElementById("product_unitary_amount_error").style.visibility = "visible"
        error = true
    }

    // Si el nombre de la unidad es vacío
    if (product_unit == "" || product_unit == "none") {
        document.getElementById("product_unit_error").innerHTML = "Debe introducir el nombre de la unidad" 
        document.getElementById("product_unit_error").style.visibility = "visible"
        error = true
    }

    product_quantity_error = document.getElementById("product_quantity_error").style.visibility
    product_unitary_amount_error = document.getElementById("product_unitary_amount_error").style.visibility

    // Solo para product_management_create 
    if (window.location.href.includes("create")) {
        product_name_error = document.getElementById("product_cod_error").style.visibility

        if (product_name_error == "visible" || product_quantity_error == "visible" || product_unitary_amount_error == "visible"){
            error = true
        }
    }

    // Solo para cupboard_management_update
    if (window.location.href.includes("update")) {
        if (product_quantity_error == "visible" || product_unitary_amount_error == "visible"){
            error = true
        }
    }

    // Si existe un error en el formulario, no se envía
    if (error) {
        if (unit_found) {
            document.getElementById("product_unit").setAttribute("disabled", 'disabled');
            document.getElementById("is_spare_part").setAttribute("disabled", 'disabled');
            unit_found = false;
        }
        return false
    }
    else {
        return true
    }
}

// Validación dinámica de la actualización de la cantidad de productos
function quantity_update_validation() {
    product_quantity_update = parseFloat(document.getElementById("product_quantity").value)
    operation_type_update = document.getElementById("operation_type").value

    product = products.find(i => i.product_name == product_name);
    current_quantity = parseInt(product.product_quantity)

    // Si la cantidad de productos introducido es menor a uno (1)
    if (product_quantity_update < 1) {
        document.getElementById("product_quantity_error").innerHTML = "Debe introducir una cantidad mayor a 0"
        document.getElementById("product_quantity_error").style.visibility = "visible"
        return
    }

    // Si la cantidad de productos introducida es mayor o igual a uno (1)
    else if (product_quantity_update >= 1) {

        // Si la cantidad de productos introducida posee decimales o es mayor que la capacidad de la BD
        if (product_quantity_update % 1 != 0 || product_quantity_update > 2147483647) {
            document.getElementById("product_quantity_error").innerHTML = "Debe introducir una cantidad de productos válida"
            document.getElementById("product_quantity_error").style.visibility = "visible"
            return
        }
        else {
            document.getElementById("product_quantity_error").style.visibility = "hidden"
        }
    }
    else {
        document.getElementById("product_quantity_error").style.visibility = "hidden"
    }

    original_operation_quantity = parseInt(original_operation_quantity)
    original_operation_type = original_operation_type

    var base_quantity

    // Dependiendo del tipo de operación, se hace una regresión acorde para tener la cantidad del producto disponible
    if (original_operation_type == "Ingreso") {
        base_quantity = current_quantity - original_operation_quantity
    }
    else {
        base_quantity = current_quantity + original_operation_quantity
    }

    // Si el nuevo tipo de operación es "ingreso"
    if (operation_type_update == "Ingreso") {

        // Si, debido a la nueva cantidad ingresada, la cantidad del producto es menor a cero (0)
        if (base_quantity + product_quantity_update < 0) {
            document.getElementById("product_quantity_error").innerHTML = "Operación inválida"
            document.getElementById("product_quantity_error").style.visibility = "visible"
        }
    }
    // Si el nuevo tipo de operación es "egreso"
    else {
        // Si, debido a la nueva cantidad egresada, la cantidad del producto es menor a cero (0) 
        if (base_quantity - product_quantity_update < 0) {
            document.getElementById("product_quantity_error").innerHTML = "La cantidad pedida excede la cantidad disponible"
            document.getElementById("product_quantity_error").style.visibility = "visible"
        }
    }
}
document.addEventListener('DOMContentLoaded', function() {
    
    document.getElementById("product_name").addEventListener("change", name_validation)
    document.getElementById("product_unitary_amount").addEventListener("change", amount_validation)
    
    // Solo para cupboard_management_create
    if (window.location.href.includes("create")) {
        document.getElementById("product_quantity").addEventListener("change", quantity_validation)
    }

    // Solo para cupboard_management_update
    if (window.location.href.includes("update")) {
        document.getElementById("operation_type").addEventListener("change", quantity_update_validation)
        document.getElementById("product_quantity").addEventListener("change", quantity_update_validation)
    }
})

// Validación dinámica del nombre del producto
function name_validation() {
    product_name = document.getElementById("product_name").value
    operation_type = document.getElementById("operation_type").value

    // Si el nombre es vacío
    if (product_name == "") {
        document.getElementById("product_name_error").innerHTML = "Debe introducir el nombre del producto"
        document.getElementById("product_name_error").style.display = "block"
    }
    else {
        document.getElementById("product_name_error").style.display = "none"
    }

    // Si la operación es un "egreso", verifico si el producto introducido existe
    if (operation_type == "Egreso") {
        found = products.find(product => product.product_name == product_name);

        if (!found) {
            document.getElementById("product_name_error").innerHTML = "El producto seleccionado no se encuentra registrado"
            document.getElementById("product_name_error").style.display = "block"
        }
    }
}

// Validación dinámica de la cantidad del producto
function quantity_validation() {
    product_quantity = document.getElementById("product_quantity").value
    operation_type = document.getElementById("operation_type").value

    // Si el monto introducido es menor o igual a cero
    if (parseInt(product_quantity) < 1) {
        document.getElementById("product_quantity_error").innerHTML = "Debe introducir una cantidad mayor a 0"
        document.getElementById("product_quantity_error").style.display = "block"
    }
    else {
        document.getElementById("product_quantity_error").style.display = "none"
    }

    // Si la operación es un "egreso", verifico la cantidad disponible del producto
    if (operation_type == "Egreso") {
        found = products.find(product => product.product_name == product_name);

        if (found) {
            if (parseInt(product_quantity) > parseInt(found.product_quantity)) {
                document.getElementById("product_quantity_error").innerHTML = "La cantidad pedida excede la cantidad disponible"
                document.getElementById("product_quantity_error").style.display = "block"
            }
            else {
                document.getElementById("product_quantity_error").style.display = "none"
            }
        }
    }
}

// Validación dinámica del monto del producto
function amount_validation() {
    product_unitary_amount = document.getElementById("product_unitary_amount").value

    // Si el monto introducido es menor a cero
    if (parseInt(product_unitary_amount) < 0) {
        document.getElementById("product_unitary_amount_error").innerHTML = "Debe introducir un precio igual o mayor a 0"
        document.getElementById("product_unitary_amount_error").style.display = "block"
    }
    else {
        document.getElementById("product_unitary_amount_error").style.display = "none"
    }
}

// Validación estática al momento de enviar el formulario
function validate() {
    error = false

    product_name = document.getElementById("product_name").value
    product_quantity = document.getElementById("product_quantity").value
    product_unitary_amount = document.getElementById("product_unitary_amount").value

    // Si el nombre del producto es vacío
    if (product_name == "") {
        document.getElementById("product_name_error").innerHTML = "Debe introducir el nombre del producto"
        document.getElementById("product_name_error").style.display = "block"
        error = true
    }

    // Si la cantidad del producto es vacía
    if (product_quantity == "") {
        document.getElementById("product_quantity_error").innerHTML = "Debe introducir una cantidad mayor a 0"
        document.getElementById("product_quantity_error").style.display = "block"
        error = true
    }

    // Si el monto del producto es vacío
    if (product_unitary_amount == "") {
        document.getElementById("product_unitary_amount_error").innerHTML = "Debe introducir un precio igual o mayor a 0"
        document.getElementById("product_unitary_amount_error").style.display = "block"
        error = true
    }

    product_quantity_error = document.getElementById("product_quantity_error").style.display
    product_unitary_amount_error = document.getElementById("product_unitary_amount_error").style.display

    // Solo para cupboard_management_create 
    if (window.location.href.includes("create")) {
        product_name_error = document.getElementById("product_name_error").style.display

        if (product_name_error == "block" || product_quantity_error == "block" || product_unitary_amount_error == "block"){
            error = true
        }
    }

    // Solo para cupboard_management_update
    if (window.location.href.includes("update")) {
        if (product_quantity_error == "block" || product_unitary_amount_error == "block"){
            error = true
        }
    }

    // Si existe un error en el formulario, no se envía
    if (error) {
        return false
    }
    else {
        return true
    }
}

// Validación dinámica de la cantidad del producto al momento de actualizar
function quantity_update_validation() {
    product_quantity_update = document.getElementById("product_quantity").value
    operation_type_update = document.getElementById("operation_type").value

    product = products.find(i => i.product_name == product_name);
    current_quantity = product.product_quantity

    // Si el monto introducido es menor o igual a cero
    if (product_quantity_update < 1) {
        document.getElementById("product_quantity_error").innerHTML = "Debe introducir una cantidad mayor a 0"
        document.getElementById("product_quantity_error").style.display = "block"
    }
    else {
        // Si la operación es "egreso", verifico el monto antes de la operación que se está modificando
        if (operation_type_update == "Egreso") {
            if (operation_type == "Ingreso") {
                base_quantity = current_quantity - parseInt(operation_quantity)
            }
            else {
                base_quantity = current_quantity + parseInt(operation_quantity)
            }

            // Si el monto a egresar es mayor al monto disponible
            if (product_quantity_update > base_quantity) {
                document.getElementById("product_quantity_error").innerHTML = "La cantidad pedida excede la cantidad disponible"
                document.getElementById("product_quantity_error").style.display = "block"
            }
            else {
                document.getElementById("product_quantity_error").style.display = "none"
            }

        }
        else {
            document.getElementById("product_quantity_error").style.display = "none"
        }
    }
}
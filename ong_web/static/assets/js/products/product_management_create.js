document.addEventListener('DOMContentLoaded', function() {
    // Verificación dinámica de campos (Create & Update)
    document.getElementById("product_cod").addEventListener("change", unit_validation)
    
})

function unit_validation() {

    product_cod = document.getElementById("product_cod").value;
    const found = products.find(product => product.product_name == product_cod);

    if (found) {
        document.getElementById("product_unit").value = found.product_unit;
        document.getElementById("product_unit").setAttribute("disabled", 'disabled');
    }

}

function validate() {
    error = false

    operation_type = document.getElementById("operation_type").value
    product_cod = document.getElementById("product_cod").value
    product_quantity = document.getElementById("product_quantity").value
    product_unitary_amount = document.getElementById("product_unitary_amount").value
    product_unit = document.getElementById("product_unit").value

    if (document.getElementById("product_unit").disabled) {
        document.getElementById("product_unit").disabled = false;
    }

    // Verificar si la operacion es valida
    if (operation_type != "Ingreso" && operation_type != "Egreso") {
        document.getElementById("operation_type_error").innerHTML = "Debe seleccionar una opción"
        document.getElementById("operation_type_error").style.display = "block"
        error = true
    }
    else {
        document.getElementById("operation_type_error").style.display = "none"
    }

    // Verificar que las unidades del producto sean válidas
    if (product_unit == "" || product_unit == "none") {
        document.getElementById("product_unit_error").innerHTML = "Debe introducir las unidades del producto"
        document.getElementById("product_unit_error").style.display = "block"
        error = true
    }
    else {
        document.getElementById("product_unit_error").style.display = "none"
    }

    // Verificar que el nombre del producto sea valido
    if (product_cod == "") {
        document.getElementById("product_cod_error").innerHTML = "Debe introducir nombre del producto"
        document.getElementById("product_cod_error").style.display = "block"
        error = true
    }
    else {
        document.getElementById("product_cod_error").style.display = "none"
    }

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

    if (error) {
        document.getElementById("product_unit").setAttribute("disabled", 'disabled');
    }

    return !error
}
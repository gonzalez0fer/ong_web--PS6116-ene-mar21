function validate() {
    error = false

    operation_type = document.getElementById("operation_type").value
    product_name = document.getElementById("product_name").value
    product_quantity = document.getElementById("product_quantity").value
    product_unitary_amount = document.getElementById("product_unitary_amount").value

    console.log(op_count)

    // Verificar si la operacion es valida
    if (operation_type != "ingreso" && operation_type != "consumo") {
        document.getElementById("operation_type_error").innerHTML = "Debe seleccionar una opción"
        document.getElementById("operation_type_error").style.display = "block"
        error = true
    }
    else {
        document.getElementById("operation_type_error").style.display = "none"
    }

    // // Verificar que el nombre del producto sea valido
    // if (product_cod == "") {
    //     document.getElementById("product_cod_error").innerHTML = "Debe introducir nombre del producto"
    //     document.getElementById("product_cod_error").style.display = "block"
    //     error = true
    // }
    // else {
    //     document.getElementById("product_cod_error").style.display = "none"
    // }

    // Verificar que la cantidad del producto sea valida
    if (product_quantity == "") {
        document.getElementById("product_quantity_error").innerHTML = "Debe introducir una cantidad válida"
        document.getElementById("product_quantity_error").style.display = "block"
        error = true
    }
    else if (parseInt(product_quantity) <= 0) {
        document.getElementById("product_quantity_error").innerHTML = "Debe introducir una cantidad mayor o igual a 0"
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
    else if (parseInt(product_unitary_amount) < 0) {
        document.getElementById("product_unitary_amount_error").innerHTML = "Debe introducir precio mayor o igual a 0"
        document.getElementById("product_unitary_amount_error").style.display = "block"
        error = true
    }
    else {
        document.getElementById("product_unitary_amount_error").style.display = "none"
    }

    // Verificar que, si la operacion es de consumo...
    if (operation_type == "consumo") {
        const found = products.find(product => product.product_name == product_name);

        if (parseInt(op_count) == 1) {
            document.getElementById("operation_type_error").innerHTML = "No puedes revertir la única ooperación existente"
            document.getElementById("operation_type_error").style.display = "block"
            error = true
        }

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
            }
        }
    }

    return !error
}
document.addEventListener('DOMContentLoaded', function() {
    // Verificación dinámica de campos (Create & Update)
    document.getElementById("activity").addEventListener("change", activity_validation)
    document.getElementById("comments").addEventListener("change", comments_validation)    
    document.getElementById("product_name").addEventListener("change", product_name_validation)    
    document.getElementById("product_quantity").addEventListener("change", product_quantity_validation)
})

// Validación dinámica de la actividad de mantenimiento
function activity_validation() {
    activity = document.getElementById("activity").value

    if (activity == "none" || activity == "") {
        document.getElementById("activity_error").innerHTML = "Introduzca la actividad de mantenimiento a realizar"
        document.getElementById("activity_error").style.visibility = "visible"
    }
    else {
        document.getElementById("activity_error").style.visibility = "hidden"
    }
}

// Validación dinámica de la descripción de mantenimiento
function comments_validation() {
    comments = document.getElementById("comments").value

    if (comments == "none" || comments == "") {
        document.getElementById("comments_error").innerHTML = "Por favor, introduzca algún comentario respecto al mantenimiento"
        document.getElementById("comments_error").style.visibility = "visible"
    }
    else {
        document.getElementById("comments_error").style.visibility = "hidden"
    }
}

// Validación dinámica del producto a usar en el mantenimiento
function product_name_validation() {
    product_name = document.getElementById("product_name").value

    if (product_name == "none") {
        document.getElementById("product_name_error").innerHTML = "Seleccione el producto a usar en el mantenimiento"
        document.getElementById("product_name_error").style.visibility = "visible"
    }
    else {
        document.getElementById("product_name_error").style.visibility = "hidden"
    }
}

// Validación dinámica de la cantidad de producto a usar
function product_quantity_validation() {
    product_quantity = document.getElementById("product_quantity").value
    product_name = document.getElementById("product_name").value
    const found = products.find(product => product.product_name == product_name);

    if (product_quantity == "none" || product_quantity == "") {
        document.getElementById("product_quantity_error").innerHTML = "Debe introducir una cantidad válida"
        document.getElementById("product_quantity_error").style.visibility = "visible"
    }
    else if (parseInt(product_quantity) < 1) {
        document.getElementById("product_quantity_error").innerHTML = "Debe introducir una cantidad válida"
        document.getElementById("product_quantity_error").style.visibility = "visible"
    }
    else if (found && parseInt(product_quantity) > parseInt(found.product_quantity)) {
        document.getElementById("product_quantity_error").innerHTML = "La cantidad pedida excede la cantidad disponible"
        document.getElementById("product_quantity_error").style.visibility = "visible"
    }
    else {
        document.getElementById("product_quantity_error").style.visibility = "hidden"
    }
}

// Función de validación del form
function validate() {
    error = false

    activity = document.getElementById("activity").value
    comments = document.getElementById("comments").value
    product_quantity = document.getElementById("product_quantity").value
    product_name = document.getElementById("product_name").value

    if (window.location.href.includes("register")) {
  
        // Caso: Se puso cantidad y nombre
        if (product_quantity && product_name) {
            
            // Encontrar el producto que se está usando
            const found = products.find(product => product.product_name == product_name);

            // Verificación de cantidad válida
            if (parseInt(product_quantity) < 1) {
                document.getElementById("product_quantity_error").innerHTML = "Debe introducir una cantidad válida"
                document.getElementById("product_quantity_error").style.visibility = "visible"
            }
            // Verificación de disponibilidad
            else if (parseInt(product_quantity) > parseInt(found.product_quantity)) {
                document.getElementById("product_quantity_error").innerHTML = "La cantidad pedida excede la cantidad disponible"
                document.getElementById("product_quantity_error").style.visibility = "visible"
            } else {
                document.getElementById("product_quantity_error").style.visibility = "hidden"
            }

        } else if (product_quantity && !product_name) {
            // Caso: Se puso cantidad pero no nombre.
            console.log("Entro aqui? Quantity: " + product_quantity + " Name: " + product_name)
            document.getElementById("product_name_error").innerHTML = "Por favor, introduzca el nombre del producto a utilizar"
            document.getElementById("product_name_error").style.visibility = "visible" 
        } else if (product_name && !product_quantity) {
            // Caso: Se puso nombre pero no cantidad
            document.getElementById("product_quantity_error").innerHTML = "Por favor, introduzca la cantidad de producto a utilizar"
            document.getElementById("product_quantity_error").style.visibility = "visible" 
        }
    }

    if (window.location.href.includes("update")) {
        // Encontrar el producto que se está usando
        const found = products.find(product => product.product_name == product_name);

        // Si se usó algun producto para el mantenimiento se tiene que verificar que...
        if (product_quantity){
            // Verificicación de cantidad válida
            if (parseInt(product_quantity) < 1 || product_quantity == "none" || product_quantity == "") {
                document.getElementById("product_quantity_error").innerHTML = "Debe introducir una cantidad válida"
                document.getElementById("product_quantity_error").style.visibility = "visible"
            }
            // Si la cantidad nueva es mayor que la vieja, entonces nueva-vieja < disponible
            else if (parseInt(old_quantity) < parseInt(product_quantity) && parseInt(product_quantity) - parseInt(old_quantity) > found.product_quantity) {     
                document.getElementById("product_quantity_error").innerHTML = "Cantidad inválida"
                document.getElementById("product_quantity_error").style.visibility = "visible"
            }
            
        }
    }

    if (activity == "none" || activity == "") {
        document.getElementById("activity_error").innerHTML = "Introduzca la actividad de mantenimiento a realizar"
        document.getElementById("activity_error").style.visibility = "visible"
    }
    else {
        document.getElementById("activity_error").style.visibility = "hidden"
    }

    if (comments == "none" || comments == "" ) {
        document.getElementById("comments_error").innerHTML = "Por favor, introduzca algún comentario respecto al mantenimiento"
        document.getElementById("comments_error").style.visibility = "visible"
    }
    else {
        document.getElementById("comments_error").style.visibility = "hidden"
    }

    // // Verificacion de uso de proucto
    // if (product_name == "none" || product_name == "") {
    //     document.getElementById("product_name_error").innerHTML = "Por favor, introduzca la cantidad de producto a utilizar"
    //     document.getElementById("product_name_error").style.visibility = "visible"    
    // }
    // else {
    //     document.getElementById("product_name_error").style.visibility = "hidden"
    // }

    activity_error = document.getElementById("activity_error").style.visibility
    comments_error = document.getElementById("comments_error").style.visibility
    product_quantity_error = document.getElementById("product_quantity_error").style.visibility
    product_name_error = document.getElementById("product_name_error").style.visibility


    if (activity_error == "visible" || comments_error == "visible" || product_quantity_error == "visible" || product_name_error == "visible"){
        error = true
    }

    return !error
}
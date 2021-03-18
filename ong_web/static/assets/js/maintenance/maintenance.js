document.addEventListener('DOMContentLoaded', function() {
    // Verificación dinámica de campos (Create & Update)
    document.getElementById("activity").addEventListener("change", activity_validation)
    document.getElementById("comments").addEventListener("change", comments_validation)    
    document.getElementById("product_name").addEventListener("change", product_name_validation)    
    document.getElementById("product_quantity").addEventListener("change", product_quantity_validation)
})

function activity_validation() {
    activity = document.getElementById("activity").value

    if (activity == "none" || activity == "") {
        document.getElementById("activity_error").innerHTML = "Introduzca la actividad de mantenimiento a realizar"
        document.getElementById("activity_error").style.display = "block"
    }
    else {
        document.getElementById("activity_error").style.display = "none"
    }
}


function comments_validation() {
    comments = document.getElementById("comments").value

    if (comments == "none" || comments == "") {
        document.getElementById("comments_error").innerHTML = "Por favor, introduzca algún comentario respecto al mantenimiento"
        document.getElementById("comments_error").style.display = "block"
    }
    else {
        document.getElementById("comments_error").style.display = "none"
    }
}

function product_name_validation() {
    product_name = document.getElementById("product_name").value

    if (product_name == "none") {
        document.getElementById("product_name_error").innerHTML = "Seleccione el producto a usar en el mantenimiento"
        document.getElementById("product_name_error").style.display = "block"
    }
    else {
        document.getElementById("product_name_error").style.display = "none"
    }
}

function product_quantity_validation() {
    product_quantity = document.getElementById("product_quantity").value

    if (parseInt(product_quantity) < 1) {
        document.getElementById("product_quantity_error").innerHTML = "Debe introducir una cantidad válida"
        document.getElementById("product_quantity_error").style.display = "block"
    }
    else {
        document.getElementById("product_quantity_error").style.display = "none"
    }
}


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
                document.getElementById("product_quantity_error").style.display = "block"
            }
            // Verificación de disponibilidad
            else if (parseInt(product_quantity) > parseInt(found.product_quantity)) {
                document.getElementById("product_quantity_error").innerHTML = "La cantidad pedida excede la cantidad disponible"
                document.getElementById("product_quantity_error").style.display = "block"
            } else {
                document.getElementById("product_quantity_error").style.display = "none"
            }

        } else if (product_quantity && !product_name) {
            // Caso: Se puso cantidad pero no nombre.
            console.log("Entro aqui? Quantity: " + product_quantity + " Name: " + product_name)
            document.getElementById("product_name_error").innerHTML = "Por favor, introduzca el nombre del producto a utilizar"
            document.getElementById("product_name_error").style.display = "block" 
        } else if (product_name && !product_quantity) {
            // Caso: Se puso nombre pero no cantidad
            document.getElementById("product_quantity_error").innerHTML = "Por favor, introduzca la cantidad de producto a utilizar"
            document.getElementById("product_quantity_error").style.display = "block" 
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
                document.getElementById("product_quantity_error").style.display = "block"
            }
            // Si la cantidad nueva es mayor que la vieja, entonces nueva-vieja < disponible
            else if (parseInt(old_quantity) < parseInt(product_quantity) && parseInt(product_quantity) - parseInt(old_quantity) > found.product_quantity) {     
                document.getElementById("product_quantity_error").innerHTML = "Cantidad inválida"
                document.getElementById("product_quantity_error").style.display = "block"
            }
            
        }
    }

    if (activity == "none" || activity == "") {
        document.getElementById("activity_error").innerHTML = "Introduzca la actividad de mantenimiento a realizar"
        document.getElementById("activity_error").style.display = "block"
    }
    else {
        document.getElementById("activity_error").style.display = "none"
    }

    if (comments == "none" || comments == "" ) {
        document.getElementById("comments_error").innerHTML = "Por favor, introduzca algún comentario respecto al mantenimiento"
        document.getElementById("comments_error").style.display = "block"
    }
    else {
        document.getElementById("comments_error").style.display = "none"
    }

    // // Verificacion de uso de proucto
    // if (product_name == "none" || product_name == "") {
    //     document.getElementById("product_name_error").innerHTML = "Por favor, introduzca la cantidad de producto a utilizar"
    //     document.getElementById("product_name_error").style.display = "block"    
    // }
    // else {
    //     document.getElementById("product_name_error").style.display = "none"
    // }

    


    


    activity_error = document.getElementById("activity_error").style.display
    comments_error = document.getElementById("comments_error").style.display
    product_quantity_error = document.getElementById("product_quantity_error").style.display
    product_name_error = document.getElementById("product_name_error").style.display


    if (activity_error == "block" || comments_error == "block" || product_quantity_error == "block" || product_name_error == "block"){
        error = true
    }

    return !error
}
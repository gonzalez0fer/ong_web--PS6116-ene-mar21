document.addEventListener('DOMContentLoaded', function() {
    var message = document.getElementById("messages")

    if (message != null) {
        setTimeout(function(){ 
            message.style.display = "none"; 
        }, 10000);
    }
})
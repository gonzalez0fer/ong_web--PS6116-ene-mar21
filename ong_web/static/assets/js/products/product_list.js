$(document).ready( function () {
    $('#product_list').DataTable({
        "language": {
            "lengthMenu": "Ver _MENU_ productos por página",
            "loadingRecords": "Cargando...",
            "processing":     "Procesando...",
            "zeroRecords": "No se encontraron productos",
            "paginate": {
                "first":      "Primero",
                "last":       "Último",
                "next":       "Siguiente",
                "previous":   "Anterior"
            },
            "info": "Mostrando _PAGE_ de _PAGES_",
            "infoEmpty": "No hay productos disponibles",
            "infoFiltered": "(Filtrado de _MAX_ total productos registrados)",
            "search":         "Buscar   :"
        },
        "order": [[0, 'asc']],
        "aLengthMenu": [ 5, 10, 15 ],
    });
} );
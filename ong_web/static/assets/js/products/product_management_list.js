$(document).ready( function () {
    $('#product_management_list').DataTable({
        "language": {
            "lengthMenu": "Ver _MENU_ operaciones por página",
            "loadingRecords": "Cargando...",
            "processing":     "Procesando...",
            "zeroRecords": "No se encontraron operaciones",
            "paginate": {
                "first":      "Primero",
                "last":       "Último",
                "next":       "Siguiente",
                "previous":   "Anterior"
            },
            "info": "Mostrando _PAGE_ de _PAGES_",
            "infoEmpty": "No hay operaciones disponibles",
            "infoFiltered": "(Filtrado de _MAX_ total operaciones registradas)",
            "search":         "Buscar   :"
        },
        "order": [[0, 'asc']],
        "aLengthMenu": [ 5, 10, 15 ],
    });
} );
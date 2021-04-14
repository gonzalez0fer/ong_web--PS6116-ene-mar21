$(document).ready( function () {
    $('#water_tanks_list').DataTable({
        "language": {
            "lengthMenu": "Ver _MENU_ tanques de agua por página",
            "loadingRecords": "Cargando...",
            "processing":     "Procesando...",
            "zeroRecords": "No se encontraron tanques de agua",
            "paginate": {
                "first":      "Primero",
                "last":       "Último",
                "next":       "Siguiente",
                "previous":   "Anterior"
            },
            "info": "Mostrando _PAGE_ de _PAGES_",
            "infoEmpty": "No hay tanques de agua disponibles",
            "infoFiltered": "(Filtrado de _MAX_ total tanques de agua registradas)",
            "search":         "Buscar   :"
        },
        "order": [[0, 'asc']],
        "aLengthMenu": [ 5, 10, 15 ],
    });
} );
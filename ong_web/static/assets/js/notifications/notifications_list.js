$(document).ready( function () {

    // Bandeja de nuevos

    $('#notifications_list_new').DataTable({
        "language": {
            "lengthMenu": "Ver _MENU_ notificaciones por página",
            "loadingRecords": "Cargando...",
            "processing":     "Procesando...",
            "zeroRecords": "No se encontraron notificaciones",
            "paginate": {
                "first":      "Primero",
                "last":       "Último",
                "next":       "Siguiente",
                "previous":   "Anterior"
            },
            "info": "Mostrando _PAGE_ de _PAGES_",
            "infoEmpty": "No hay notificaciones disponibles",
            "infoFiltered": "(Filtrado de _MAX_ total notificaciones registradas)",
            "search":         "Buscar   :"
        },
        "order": [[0, 'asc']],
        "aLengthMenu": [ 5, 10, 15 ],
    });

    // Bandeja de leídos

    $('#notifications_list_read').DataTable({
        "language": {
            "lengthMenu": "Ver _MENU_ notificaciones por página",
            "loadingRecords": "Cargando...",
            "processing":     "Procesando...",
            "zeroRecords": "No se encontraron notificaciones",
            "paginate": {
                "first":      "Primero",
                "last":       "Último",
                "next":       "Siguiente",
                "previous":   "Anterior"
            },
            "info": "Mostrando _PAGE_ de _PAGES_",
            "infoEmpty": "No hay notificaciones disponibles",
            "infoFiltered": "(Filtrado de _MAX_ total notificaciones registradas)",
            "search":         "Buscar   :"
        },
        "order": [[0, 'asc']],
        "aLengthMenu": [ 5, 10, 15 ],
    });
} );
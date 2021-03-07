$(document).ready( function () {
    $('#equipment_list').DataTable({
        "language": {
            "lengthMenu": "Ver _MENU_ equipos por página",
            "loadingRecords": "Cargando...",
            "processing":     "Procesando...",
            "zeroRecords": "No se encontraron equipos",
            "paginate": {
                "first":      "Primero",
                "last":       "Último",
                "next":       "Siguiente",
                "previous":   "Anterior"
            },
            "info": "Mostrando _PAGE_ de _PAGES_",
            "infoEmpty": "No hay equipos disponibles",
            "infoFiltered": "(Filtrado de _MAX_ total equipos registrados)",
            "search":         "Buscar   :"
        },
        "order": [[0, 'asc']],
        "aLengthMenu": [ 5, 10, 15 ],
    });
} );
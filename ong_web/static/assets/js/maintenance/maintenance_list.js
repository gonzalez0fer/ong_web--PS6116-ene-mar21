$(document).ready( function () {
    $('#maintenance_list').DataTable({
        "language": {
            "lengthMenu": "Ver _MENU_ mantenimientos por página",
            "loadingRecords": "Cargando...",
            "processing":     "Procesando...",
            "zeroRecords": "No se encontraron record de mantenimiento",
            "paginate": {
                "first":      "Primero",
                "last":       "Último",
                "next":       "Siguiente",
                "previous":   "Anterior"
            },
            "info": "Mostrando _PAGE_ de _PAGES_",
            "infoEmpty": "No hay mantenimientos disponibles",
            "infoFiltered": "(Filtrado de _MAX_ total mantenimientos registrados)",
            "search":         "Buscar   :"
        },
        "order": [[0, 'asc']],
        "aLengthMenu": [ 5, 10, 15 ],
    });
} );
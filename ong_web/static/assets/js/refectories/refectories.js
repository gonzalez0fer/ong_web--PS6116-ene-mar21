$(document).ready( function () {
    $('#refectories_list').DataTable({
        "language": {
            "lengthMenu": "Ver _MENU_ centros de distribución por página",
            "loadingRecords": "Cargando...",
            "processing":     "Procesando...",
            "zeroRecords": "No se encontraron centros de distribución",
            "paginate": {
                "first":      "Primero",
                "last":       "Último",
                "next":       "Siguiente",
                "previous":   "Anterior"
            },
            "info": "Mostrando _PAGE_ de _PAGES_",
            "infoEmpty": "No hay centros de distribución disponibles",
            "infoFiltered": "(Filtrado de _MAX_ total centros de distribución registrados)",
            "search":         "Buscar   :"
        },
        "order": [[0, 'asc']],
        "aLengthMenu": [ 5, 10, 15 ],
    });
} );
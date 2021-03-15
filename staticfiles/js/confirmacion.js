function confirmacionEliminacionproducto(id){
    Swal.fire({
        title: '¿Estas seguro?',
        text: "No podras desacer esta acción",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si eliminar',
        cancelButtonText: 'Cancelar'
      }).then((result) => {
        if (result.isConfirmed) {
          window.location.href = "/eliminar_producto/"+id+"";
        }
      })
}

function confirmacionEliminacioncomercio(id){
  Swal.fire({
      title: '¿Estas seguro?',
      text: "No podras desacer esta acción",
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: 'Si eliminar',
      cancelButtonText: 'Cancelar'
    }).then((result) => {
      if (result.isConfirmed) {
        window.location.href = "/eliminar_comercio/"+id+"";
      }
    })
}
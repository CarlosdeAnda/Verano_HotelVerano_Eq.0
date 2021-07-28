function comprobar(){
    
    formDatos = {};
    mensaje = ""
    aux=true
    formDatos[0] = document.getElementById('inputLugar').value
    formDatos[1] = document.getElementById('inputPiso').value
    
    for (const key in formDatos) { //Recorre todo los campos del formulario.

        if(formDatos[key] == "Selecciona una opción..."){ //Verifica si los campos estan vacios y si es así devuelve un error y en la variable aux devuelve un false.
            mensaje = mensaje + "Alguno de los campos esta vacio. \n\n"
            aux =false;
            break;
        }
    }

    if(aux){
        document.getElementById("btn-registrar").style.display = 'block';
        document.getElementById("btn-comprobar").style.display = 'none';

    }
    else{
        var modal = $('#errorModal')
        modal.find('.modal-title').text("Error")
        modal.find('.modal-body').text(mensaje)
        modal.modal('show')

    }

}



function comprobar(){
    
    formDatos = {};
    mensaje = ""
    aux=true
    formDatos[0] = document.getElementById('inputNombre').value
    formDatos[1] = document.getElementById('inputApellidoPaterno').value
    formDatos[2] = document.getElementById('inputApellidoMaterno').value
    formDatos[3] = document.getElementById('inputFechaRegistro').value
    formDatos[4] = document.getElementById('inputTelefono').value
    formDatos[5] = document.getElementById('inputcorreo').value
    formDatos[6] = document.getElementById('inputDireccion').value


    for (const key in formDatos) { //Recorre todo los campos del formulario.

        if(formDatos[key] == ""){ //Verifica si los campos estan vacios y si es así devuelve un error y en la variable aux devuelve un false.
            mensaje = mensaje + "Alguno de los campos esta vacio. \n\n"
            aux =false;
            break;
        }
    }
    if(!validarTelefono(formDatos[4])){
        mensaje = mensaje + "El telefono es incorrecto. \n\n"
        aux =false;
    }

    if(!validarCorreo(formDatos[5])){
        mensaje = mensaje + "El correo es invalido. \n\n"
        aux =false;
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



function validarDigito(valor){                  
    var regex = /^\d+$/                                                  
    var response = regex.test(valor)                                                           
    return response;                                                                        
}   

function validarTelefono(valor){                                
    var regex = /^\d{3}-\d{3}-\d{4}$/                                                     
    var response = regex.test(valor)                                            
    return response;                                                                        
}   

function validarCorreo(valor){                                
    var regex = /^\w[a-zA-Z\s]*$/                                                     
    var response = regex.test(valor)                                            
    return response;                                                                        
}   

function logitudUsuario(valor){                                
    var regex = /^\w{8,}/                                                     
    var response = regex.test(valor)                                            
    return response;                                                                        
}

function logitudnss(valor){                                
    var regex = /^\d{10}$/                                                     
    var response = regex.test(valor)                                            
    return response;                                                                        
}
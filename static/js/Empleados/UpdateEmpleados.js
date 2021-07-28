function comprobar(){
    
    formDatos = {};
    mensaje = ""
    aux=true
    formDatos[0] = document.getElementById('inputNombre').value
    formDatos[1] = document.getElementById('inputApellidoPaterno').value
    formDatos[2] = document.getElementById('inputApellidoMaterno').value
    formDatos[3] = document.getElementById('inputGenero').value
    formDatos[4] = document.getElementById('inputFechaNacimiento').value
    formDatos[5] = document.getElementById('inputFechaRegistro').value
    formDatos[6] = document.getElementById('inputTelefono').value
    formDatos[7] = document.getElementById('inputTipo').value
    formDatos[8] = document.getElementById('inputUsuario').value
    formDatos[9] = document.getElementById('inputPassword1').value
    formDatos[10] = document.getElementById('inputPassword2').value
    

    for (const key in formDatos) { //Recorre todo los campos del formulario.

        if(formDatos[key] == ""){ //Verifica si los campos estan vacios y si es así devuelve un error y en la variable aux devuelve un false.
            mensaje = mensaje + "Alguno de los campos esta vacio. \n\n"
            aux =false;
            break;
        }
    }

    if(formDatos[9] != formDatos[10]){
        mensaje = mensaje + "Las contraseñas no coinciden. \n\n"
        aux =false;
    }



    if(!ValidarString(formDatos[1])){
        mensaje = mensaje + "El apellido paterno tiene un formato incorrecto. \n\n"
        aux =false;
    }

    if(!ValidarString(formDatos[2])){
        mensaje = mensaje + "El apellido materno tiene un formato incorrecto. \n\n"
        aux =false;
    }


    if(!validarTelefono(formDatos[6])){
        mensaje = mensaje + "El telefono es incorrecto. \n\n"
        aux =false;
    }


    if(!logitudUsuario(formDatos[8])){
        mensaje = mensaje + "El usuario debe tener una longitud de 8 caracteres. \n\n"
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


function ValidarString(valor){                                
    var regex = /^[\w'\-,.][^0-9_!¡?÷?¿\\+=@#$%ˆ&*(){}|~<>;:[\]]{2,}$/                                                     
    var response = regex.test(valor)                                            
    return response;                                                                        
}

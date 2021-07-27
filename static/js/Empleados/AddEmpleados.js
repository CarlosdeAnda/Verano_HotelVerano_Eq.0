var extValidas = [".jpg", ".jpeg",".png"];                                                                                                                                 


function ValidarArchivo(oninput) { //Verifica las extenciones de lo archivos.                                                                                                                                                      
    if (oninput.type == "file") {  // S                                                                                                                                                           
        var nombre = oninput.value;                                                                                                                                   
         if (nombre.length > 0) {                                                                                                                                                              
            var bandera = false;                                                                                                                                               
            for (var j = 0; j < extValidas.length; j++) {                                                                                                                  
                var sCurExtension = extValidas[j];                              
                if (nombre.substr(nombre.length - sCurExtension.length, sCurExtension.length).toLowerCase() == sCurExtension.toLowerCase()) {                                         
                    bandera = true;                            
                    break;                                                                                                                                                                      
                }                                                                                                                                                                                 
            }                                                                  
                                                                        
            if (!bandera) {    
                var modal = $('#errorfileModal')
                modal.find('.modal-title').text("Error")
                modal.find('.modal-body').text("Solo se permiten archivos con extenciones: jpg,png,jpeg.")
                modal.modal('show')                                                                                                                                     
                oninput.value = "";                                             
                return false;                                   
            }                                                                  
        }                                                                           
    }                                                                               
    return true;                                                        
}   



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
    formDatos[11] = document.getElementById('inputFoto').value

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


    if(!validarString(formDatos[0])){
        mensaje = mensaje + "El nombre debe ser solo letras. \n\n"
        aux =false;
    }

    if(!validarTelefono(formDatos[6])){
        mensaje = mensaje + "El telefono es incorrecto. \n\n"
        aux =false;
    }

    if(!validarString(formDatos[1])){
        mensaje = mensaje + "El apellido paterno debe ser solo letras. \n\n"
        aux =false;
    }

    if(!validarString(formDatos[2])){
        mensaje = mensaje + "El apellido materno debe ser solo letras \n\n"
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

function validarString(valor){
    var regex= /^\w[a-zA-Z]+\s?\w[a-zA-Z]+\s?\w[a-zA-Z]+$/
    var response = regex.test(valor)                                                           
    return response;            
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
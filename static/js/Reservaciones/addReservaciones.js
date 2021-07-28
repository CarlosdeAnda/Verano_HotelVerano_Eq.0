


function comprobar(){
    
    formDatos = {};
    mensaje = ""
    aux=true
    formDatos[0] = document.getElementById('inputEmpleado').value
    formDatos[1] = document.getElementById('inputCliente').value
    formDatos[2] = document.getElementById('inputDisponibles').value
    formDatos[3] = document.getElementById('inputFechaIngreso').value
    formDatos[4] = document.getElementById('inputFechaSalida').value
    formDatos[5] = document.getElementById('inputLugar').value


    for (const key in formDatos) { //Recorre todo los campos del formulario.
        
        if(formDatos[key] == ""){ //Verifica si los campos estan vacios y si es así devuelve un error y en la variable aux devuelve un false.
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
    var regex = /^\w[a-zA-Z.-_$,]+@\w[a-zA-Z]+\.\w[a-zA-Z]+\.?\w+/                                                     
    var response = regex.test(valor)                                            
    return response;                                                                        
}   

function logitudUsuario(valor){                                
    var regex = /^\w{8,}/                                                     
    var response = regex.test(valor)                                            
    return response;                                                                        
}

function ValidarString(valor){                                
    var regex = /^[\w'\-,.][^0-9_!¡?÷?¿\\+=@#$%ˆ&*(){}|~<>;:[\]]{2,}$/                                                     
    var response = regex.test(valor)                                            
    return response;                                                                        
}

function logitudnss(valor){                                
    var regex = /^\d{10}$/                                                     
    var response = regex.test(valor)                                            
    return response;                                                                        
}
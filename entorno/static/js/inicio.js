const open_ingreso = document.getElementById('open_ingreso');
const open_registro = document.getElementById('open_registro');
const modal_container_ingreso = document.getElementById('modal_container_ingreso');
const close_ingreso = document.getElementById('close_ingreso');
const close_registro = document.getElementById('close_registro');
const ingreso_registro = document.getElementById('ingreso_registro');
const registro_ingreso = document.getElementById('registro_ingreso');
const aceptar_ingreso = document.getElementById('aceptar_ingreso');
const aceptar_registro = document.getElementById('aceptar_registro');

open_ingreso.addEventListener('click', () => {
    modal_container_ingreso.classList.add('show_ingreso');
});

close_ingreso.addEventListener('click', () => {
    modal_container_ingreso.classList.remove('show_ingreso');
});

open_registro.addEventListener('click', () => {
    modal_container_registro.classList.add('show_registro');
});

close_registro.addEventListener('click', () => {
    modal_container_registro.classList.remove('show_registro');
});

ingreso_registro.addEventListener('click', () => {
    modal_container_ingreso.classList.remove('show_ingreso');
    modal_container_registro.classList.add('show_registro');
});

registro_ingreso.addEventListener('click', () => {
    modal_container_registro.classList.remove('show_registro');
    modal_container_ingreso.classList.add('show_ingreso');
});

aceptar_ingreso.addEventListener('click', () => {
    var inputEmail = document.formulario_ingreso.correoingreso;
    var inputPass = document.formulario_ingreso.passwordingreso;
    
    var userEmail = inputEmail.value;
    var userPass = inputPass.value;
    var formato_email = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)(\.\w{2,3})+$/;
    
    if(!userEmail.match(formato_email))
    {
        alert("Escriba un correo valido");
        inputEmail.focus();
        return false;
    }

    if(userPass.length < 8 || userPass.length == 0)
    {
        alert("La contraseña debe tener minimo 8 caracteres");
        inputPass.focus();
        return false;
    }
    //alert ('Prueba validar ingreso');
//    window.location = "menu";

});    

aceptar_registro.addEventListener('click', () => {
    var inputName = document.formulario_registro.nombreregistro;
    var inputLastN = document.formulario_registro.apellidoregistro;
    var inputEmail = document.formulario_registro.correoregistro;
    var inputPass = document.formulario_registro.passwordregistro;
    var inputConfPass = document.formulario_registro.confirmpasswordregistro;
    
    var userName = inputName.value;
    var userLastN = inputLastN.value;
    var userEmail = inputEmail.value;
    var userPass = inputPass.value;
    var userConfPass = inputConfPass.value;
    var formato_email = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)(\.\w{2,3})+$/;
    
    if(userName.length == 0)
    {
        alert("Nombre invalido");
        inputName.focus();
        return false;
    }
    if(userLastN.length == 0)
    {
        alert("Apellido invalido");
        inputLastN.focus();
        return false;
    }
    if(!userEmail.match(formato_email))
    {
        alert("Escriba un correo valido");
        inputCorreo.focus();
        return false;
    }

    if(userPass.length < 8 || userPass.length == 0)
    {
        alert("La contraseña debe tener minimo 8 caracteres");
        inputPass.focus();
        return false;
    }
    if(!userConfPass.match(userPass))
    {
        alert("Las contraseñas no coinciden");
        inputConfPass.focus();
        return false;
    }
    //alert ('Prueba validar registro');
//    window.location = "menu";
}); 

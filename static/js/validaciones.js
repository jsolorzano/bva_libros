$(document).ready(function() {
    
    $("form").attr('autocomplete','off');
    $('#id_send').hide();
    $("input:submit,input:file,input:reset").attr('class','btn btn-primary');
    $("input:text,select,textarea,input:password").attr('class','form-control');
    $("#id_cedula_gren").numeric({allow: " "}).attr('maxlength','9').focus();
    $("#id_p_nombre").alpha({allow: " "});
    $("#id_s_nombre").alpha({allow: " "})
    $("#id_p_apellido").alpha({allow: " "});
    $("#id_s_apellido").alpha({allow: " "});
    $("#id_fecha_nac").numeric({allow: "/"}).attr('maxlength','10');
    $("#id_edad").numeric({allow: ""});
    $("#id_tlf_movil").numeric({allow: ""}).attr('maxlength','11');
    $("#id_tlf_local").numeric({allow: ""}).attr('maxlength','11');
    $("#id_marca_m").alphanumeric({allow: " !°#$%&/()=?¡-_[]¨+"});
    $("#id_modelo_m").alphanumeric({allow: " !°#$%&/()=?¡-_[]¨+"});
    $("#id_color_m").alpha({allow: " "});
    $("#id_ano_m").numeric({allow: " "}).attr('maxlength','4');
    $("#id_placa_m").alphanumeric({allow: " !°#$%&/()=?¡-_[]¨+"});
    $("#id_serial_c_m").alphanumeric({allow: " !°#$%&/()=?¡-_[]¨+"});
    $("#id_serial_moto_c").alphanumeric({allow: " !°#$%&/()=?¡-_[]¨+"});
    $("#id_especifique").alpha({allow: " "});
    $("#id_cedula_d_o").numeric({allow: "/"}).attr('maxlength','9');
    $("#id_p_nombre_d_o").alpha({allow: " "});
    $("#id_s_nombre_d_o").alpha({allow: " "});
    $("#id_p_apellido_d_o").alpha({allow: " "});
    $("#id_s_apellido_d_o").alpha({allow: " "});
    $("#id_tlf_d_o").numeric({allow: ""}).attr('maxlength','11');
    $("#id_obs_d_o").alpha({allow: " "});
    $("#id_nom_c").alpha({allow: " "});
    $("#id_nom_linea").alpha({allow: " "});
    $("#id_tlf_l").numeric({allow: ""}).attr('maxlength','11');
    $("#id_carga_f").numeric({allow: ""});
    $("#id_fam_disc").numeric({allow: ""});
    $("#id_s_habitacional").alpha({allow: " "});
    /* alphanumeric */
    
    
    // INICIO. VALIDACIONES Y FUNCIONES DE LOS TEMPLATE DEL MÓDULO DE DIRECTIVA--------------------------------------
    // Función para la carga de datos de agremiado solicitado por su cédula
    $("#id_cedula").change(function() {
	var cedula = $(this).val();
       
	if (cedula != '') {
	    $.get('/directiva/busqueda_agremiado/', {'cedula':cedula}, function(data) {
                //console.log(data[0]) // Imprime en la consola javascript
                //alert(String(data[0]));
                if (data != 0) {
                    var n = data[0].fields.nacionalidad;
                    var ced = data[0].fields.cedula;
                    var p_n = data[0].fields.p_nombre;
                    var p_a = data[0].fields.p_apellido;
                    //var est = data[0].fields.estado;
                    //var mun = data[0].fields.municipio;
                    var tel = data[0].fields.tlf_movil;
                    
                    $('#id_nac').val(n);
                    $('#id_cedula').val(ced);
                    $('#id_nombre').val(p_n);
                    $('#id_apellido').val(p_a);
                    //$('#id_cod_estado').val(est);
                    //$('#id_cod_municipio').val(mun);
                    $('#id_telefono').val(tel);
                }else{
                    apprise('No se encontro el agremiado');
                    $('#id_nac').val('V');
                    $('#id_cedula').val('');
                    $('#id_nombre').val('');
                    $('#id_apellido').val('');
                    //$('#id_cod_estado').val(0);
                    //$('#id_cod_municipio').val(0);
                    $('#id_telefono').val('');
                }
                
	    }, 'json');
	}
	
    });
    
    // Función para la fijación del nivel del cargo seleccionado
    $("#id_cargo").change(function() {
        var cargo = $(this).val();
		// Evaluamos el nivel obtenido y habilitamos los campos necesarios
		if (cargo == 'C0005') {
			$('#id_coord').val('S');
		}else{
			$('#id_coord').val('N');
		}
    });
    
    // Función para la fijación del nivel del cargo seleccionado
    $("#id_coord").change(function() {
        var coord = $(this).val();
        
        if (coord == 'N') {
            $('#id_area').val('A0000');
        }
    });
    
    // Función para la habilitación de los combos de estado y municipio según el area seleccionada
    $("#id_area").change(function() {
        var area = $(this).val();
        
        if (area != 'A0005') {
            $('#id_cod_estado').val(4);
            $('#id_cod_municipio').val(0);
        }
    });
    // CIERRE. VALIDACIONES Y FUNCIONES DE LOS TEMPLATE DEL MÓDULO DE DIRECTIVA--------------------------------------
    
        /*Validacion para reflejar los datos pertenecientes del agremiado
           atraves de una petición del sistema de consulta y calcular
           de forma automatica la edad
        */
        
        
        $("#id_cedula_gren").change(function(event){
            var cedula = $('#id_cedula_gren').val();                        
            var hosting = $('#id_hosting').val(); // Captura del hosting (dominio)
            
            if (hosting) {
                
                $.get("http://"+hosting+""+cedula+"", function(data) {
                    var option = "";
                    $.each(data, function(i) {
                    
                        $("#id_p_nombre").val(data[i].p_nombre)
                        $("#id_s_nombre").val(data[i].s_nombre)
                        $("#id_p_apellido").val(data[i].p_apellido)
                        $("#id_s_apellido").val(data[i].s_apellido)
                        $("#id_fecha_nac").val(data[i].f_nac)
                        $("#id_sexo").val(data[i].sexo.substring(0,1))
                        $('#id_ins_cne').val('1');
                        //alert(data[i].sexo.substring(0,1));
                        /* Validacion para calcular la edad de forma automatica*/
                        var fechaActual = new Date()
                        var diaActual = fechaActual.getDate();
                        var mmActual = fechaActual.getMonth() + 1;
                        var yyyyActual = fechaActual.getFullYear();
                        
                        FechaNac = data[i].f_nac.split("/");
                        var diaCumple = FechaNac[0];
                        var mmCumple = FechaNac[1];
                        var yyyyCumple = FechaNac[2];
                        //alert("DIA: "+diaCumple);
                        //retiramos el primer cero de la izquierda
                        if (mmCumple.substr(0,1) == 0) {
                            mmCumple= mmCumple.substring(1, 2);
                        }
                        //retiramos el primer cero de la izquierda
                        if (diaCumple.substr(0, 1) == 0) {
                            diaCumple = diaCumple.substring(1, 2);
                        }
                        var edad = yyyyActual - yyyyCumple;
                        
                        /*validamos si el mes de cumpleaños es menor al actual
                        o si el mes de cumpleaños es igual al actual
                        y el dia actual es menor al del nacimiento
                        De ser asi, se resta un año*/
                        if ((mmActual < mmCumple) || (mmActual == mmCumple && diaActual < diaCumple)) {
                        edad--;
                        }
                        $("#id_edad").val(edad);
                        });
                    // Proceso para validar con la clase error 404 Not Found
                    },'json').error(function(){

                
                apprise('No se encuentra registrado en el cne, ¿desea continuar?', {'verify':true}, function(r)
                {
                if(r)
                    {
                    $("#id_cedula_gren").focus();
                    $("#id_p_nombre").val('');
                    $("#id_s_nombre").val('');
                    $("#id_p_apellido").val('');
                    $('#id_s_apellido').val('');
                    $('#id_fecha_nac').val('');
                    $('#id_edad').val('');
                    $('#id_ins_cne').val('');
                    $('#id_sexo').val('');
                    $('#id_ins_cne').val('2');
                    
                    }
                else
                    {
                    $("#id_cedula_gren").val('');
                    $("#id_cedula_gren").focus();
                    $("#id_p_nombre").val('');
                    $("#id_s_nombre").val('');
                    $("#id_p_apellido").val('');
                    $('#id_s_apellido').val('');
                    $('#id_fecha_nac').val('');
                    $('#id_edad').val('');
                    $('#id_ins_cne').val('');
                    $('#id_sexo').val('');
                    $('#id_ins_cne').val('2');
                    
                    }
                });
                
            });
            
                }else{
                    apprise("Disculpe, dominio no disponible, contacte al administrador del sistema...");
                    $("#id_cedula_gren").val('');
                }
	});
        
        /* Validacion para habilitar los datos del propietario si selecciona si*/
        $("#id_documentos").change(function(event){
            doc = $("#id_documentos").val();
            if (doc == '2') {
                $("#id_cedula_d_o").val("")
                $("#id_p_nombre_d_o").val("")
                $("#id_s_nombre_d_o").val("")
                $("#id_p_apellido_d_o").val("")
                $("#id_s_apellido_d_o").val("")
                $("#id_tlf_d_o").val("");
                $("#id_direccion_d_o").val("");
                
            }else{
                //alert("No Selecciono");
                //$('#datos_propietario').hide();
                var cedula = $('#id_cedula_gren').val();
                var movil = $("#id_tlf_movil").val();
                var dir = $("#id_direccion").val();
                var hosting = $('#id_hosting').val();
                $.get("http://"+hosting+""+cedula+"", function(data) {
                    var option = "";
                    $.each(data, function(i) {
                        $("#id_cedula_d_o").val(data[i].cedula)
                        $("#id_p_nombre_d_o").val(data[i].p_nombre)
                        $("#id_s_nombre_d_o").val(data[i].s_nombre)
                        $("#id_p_apellido_d_o").val(data[i].p_apellido)
                        $("#id_s_apellido_d_o").val(data[i].s_apellido)
                        $("#id_tlf_d_o").val(movil);
                        $("#id_direccion_d_o").val(dir);
                    });
                });
            }
        });
        
        // Validacion para habilitar y desabilitar el campo de partido politico
        $("#id_partido").change(function() {
        var partido = $(this).val();
        
        if (partido == '1') {
            $('#id_partido_p').prop('disabled', false);
        }else{
            $('#id_partido_p').prop('disabled', true);
            $('#id_partido_p').val("");
        }
        });
        
        // Validacion para habilitar y sesabilitar el campo se encuentra a su nombre
        $("#id_documentos").change(function() {
        var d_nom = $(this).val();
        
            if (d_nom == '2') {
                $('#id_especifique').prop('disabled', false);
            }else{
                $('#id_especifique').prop('disabled', true);
            }
        });
        
        // Validacion para habilitar y desabilitar el campo Observacion, segun lo que escoja
        $("#id_traspaso").change(function() {
        var traspaso = $(this).val();
            
            if (traspaso == '2') {
                $('#id_obs_d_o').prop('disabled', false);
            }else{
                $('#id_obs_d_o').prop('disabled', true);
            }
        
        });
        
        
        // Validacion para asignar un codigo a un agremiado segun el estatus
        $("#id_c_agremiado").change(function() {
        var c_agremiado = $(this).val();
        //alert("CODIGO: "+c_agremiado);
        $.get('/registro/ajax_b_codigo/', {'c_agremiado':c_agremiado}, function(data) {
            //alert(data);
                $.each(data, function(i) {
                    if (data[0]!=0) {
                        
                        apprise('El código ya se encuentra asignado...');
                        $("#id_c_agremiado").val('').focus();
                    }
                });
            });
        });
        
        // Validacion para reflejar las lineas a un agremiado
        
        $("#id_nom_linea_gren").change(function(){
            c_linea = $(this).val();
            
            if (c_linea!=0) {
            
                $.get('/registro/ajax_linea/', {'c_linea':c_linea}, function(data) {
                
                    $.each(data, function(i) {
                        //alert(data[i].fields.direccion);
                        $("#id_nom_c").val(data[i].fields.presidente);
                        $("#id_tlf_l").val(data[i].fields.telefono);
                        $("#id_direccion_p_r").val(data[i].fields.direccion);
                    });
                });
            }else{
                apprise("Disculpe debe seleccionar una linea...");
                $("#id_nom_c").val('');
                $("#id_tlf_l").val('');
                $("#id_direccion_p_r").val('');
            }
        })
        
        // Validacion de campos, acceder a elementos del DOM DIV
        
        $('input#sub_mit_data').click(function(){
            
            if ($("#id_cedula_gren").val() == ""){
                apprise("Ingrese la cedula");
                $('#id_cedula_gren').focus();
                return false;
            }
            else if ($("#id_c_agremiado").val() == ""){
                apprise("Ingrese el código");
                $('#id_c_agremiado').focus();
                return false;
            }
            else if ($("#id_foto_add").val() == ""){
                apprise("Ingrese la foto");
                $('#id_foto_add').focus();
                return false;
            }
            else if ($("#id_sexo").val() == ""){
                apprise("Seleccione el sexo");
                $('#id_sexo').focus();
                return false;
            }
            else if ($("#id_status").val() == "" || $("#id_status_mod").val() == ""){
                apprise("Seleccione el Estátus");
                $("#id_status").focus();
                $("#id_status_mod").focus();
                return false; 
            }
            else if ($("#id_p_nombre").val() == ""){
                apprise("Ingrese el primer nombre");
                $("#id_p_nombre").focus();
                return false; 
            }
            else if ($("#id_p_nombre").val() == ""){
                apprise("Ingrese el primer nombre");
                $("#id_p_nombre").focus();
                return false; 
            }
            else if ($("#id_p_apellido").val() == ""){
                apprise("Ingrese el primer apellido");
                $("#id_p_apellido").focus();
                return false; 
            }
            else if ($("#id_fecha_nac").val() == ""){
                apprise("Ingrese la fecha de nacimiento");
                $("#id_fecha_nac").focus();
                return false; 
            }
            else if ($("#id_edad").val() == ""){
                apprise("Ingrese la edad");
                $("#id_edad").focus();
                return false; 
            }
            else if ($("#id_tlf_movil").val() == ""){
                apprise("Ingrese el teléfono");
                $("#id_tlf_movil").focus();
                return false; 
            }
            else if ($("#id_t_camisa").val() == ""){
                apprise("Ingrese la talla de la camisa");
                $("#id_t_camisa").focus();
                return false; 
            }
            else if ($("#id_cod_estado").val() == ""){
                alert("Seleccione el estado en datos de habitación");
                $('#datos_h').attr('class','alert alert-danger');
                $('#datos_s').attr('class','alert');
                $('#documentos_c').attr('class','alert');
                $('#datos_l').attr('class','alert');
                $("#id_cod_estado").focus();
                return false; 
            }
            else if ($("#id_cod_municipio").val() == ""){
                apprise("Seleccione el municipio en datos de habitación");
                $('#datos_h').attr('class','alert alert-danger');
                $('#datos_s').attr('class','alert');
                $('#documentos_c').attr('class','alert');
                $('#datos_l').attr('class','alert');
                $("#id_cod_municipio").focus();
                return false; 
            }
            else if ($("#id_cod_parroquia").val() == ""){
                alert("Seleccione la parroquia en datos de habitación");
                $('#datos_h').attr('class','alert alert-danger');
                $('#datos_s').attr('class','alert');
                $('#documentos_c').attr('class','alert');
                $('#datos_l').attr('class','alert');
                $("#id_cod_parroquia").focus();
                return false; 
            }
            else if ($("#id_direccion").val() == ""){
                apprise("Ingrese la dirección en datos de habitación");
                $('#datos_h').attr('class','alert alert-danger');
                $('#datos_s').attr('class','alert');
                $('#documentos_c').attr('class','alert');
                $('#datos_l').attr('class','alert');
                $("#id_direccion").focus();
                return false; 
            }
            else if ($("#id_discapcidad").val() == ""){
                apprise("Seleccione si posee discapacidad en datos sociopolítico");
                $('#datos_h').attr('class','alert');
                $('#documentos_c').attr('class','alert');
                $('#datos_l').attr('class','alert');
                $('#datos_s').attr('class','alert alert-danger');
                $("#id_discapcidad").focus();
                return false;
            }
            else if ($("#id_s_habitacional_gren").val() == ""){
                apprise("Seleccione situación habitacional en datos sociopolítico");
                 $('#datos_h').attr('class','alert');
                $('#documentos_c').attr('class','alert');
                $('#datos_l').attr('class','alert');
                $('#datos_s').attr('class','alert alert-danger');
                $("#id_s_habitacional_gren").focus();
                return false;
            }
            else if ($("#id_ins_cne").val() == ""){
                apprise("¿Esta inscrito en el cne? en datos sociopolítico");
                 $('#datos_h').attr('class','alert');
                $('#documentos_c').attr('class','alert');
                $('#datos_l').attr('class','alert');
                $('#datos_s').attr('class','alert alert-danger');
                $("#id_ins_cne").focus();
                return false;
            }
            else if ($("#id_partido").val() == ""){
                apprise("¿Milita en algun partido? en datos sociopolítico");
                 $('#datos_h').attr('class','alert');
                $('#documentos_c').attr('class','alert');
                $('#datos_l').attr('class','alert');
                $('#datos_s').attr('class','alert alert-danger');
                $("#id_partido").focus();
                return false;
            }
            else if ($("#id_organizacion").val() == ""){
                apprise("¿Milita en alguna organización? en datos sociopolítico");
                 $('#datos_h').attr('class','alert');
                $('#documentos_c').attr('class','alert');
                $('#datos_l').attr('class','alert');
                $('#datos_s').attr('class','alert alert-danger');
                $("#id_organizacion").focus();
                return false;
            }
            else if ($("#id_licencia").val() == ""){
                apprise("¿Posee licencia? en Documentos para conducir");
                $('#datos_h').attr('class','alert');
                $('#datos_s').attr('class','alert');
                $('#documentos_c').attr('class','alert alert-danger');
                $("#id_licencia").focus();
                return false;
            }
            else if ($("#id_certificado").val() == ""){
                apprise("¿Posee certificado? en Documentos para conducir");
                $('#datos_h').attr('class','alert');
                $('#datos_s').attr('class','alert');
                $('#documentos_c').attr('class','alert alert-danger');
                $("#id_certificado").focus();
                return false;
            }
            else if ($("#id_poliza_rcv").val() == ""){
                apprise("¿Posee poliza RCV? en Documentos para conducir");
                $('#datos_h').attr('class','alert');
                $('#datos_s').attr('class','alert');
                $('#documentos_c').attr('class','alert alert-danger');
                $("#id_poliza_rcv").focus();
                return false;
            }
            else if ($("#id_documentos").val() == ""){
                apprise("¿Se encuentra a su nombre? en Documentos para conducir");
                $('#datos_h').attr('class','alert');
                $('#datos_s').attr('class','alert');
                $('#documentos_c').attr('class','alert alert-danger');
                $("#id_documentos").focus();
                return false;
            }
            //else if ($("#id_cedula_d_o").val() == ""){
            //    alert("¿Ingrese la cédula en Documentos para conducir");
            //    $('#datos_h').attr('class','alert');
            //    $('#datos_s').attr('class','alert');
            //    $('#documentos_c').attr('class','alert alert-danger');
            //    $("#id_cedula_d_o").focus();
            //    return false;
            //}
            //else if ($("#id_p_nombre_d_o").val() == ""){
            //    alert("¿Ingrese el primer nombre en Documentos para conducir");
            //    $('#datos_h').attr('class','alert');
            //    $('#datos_s').attr('class','alert');
            //    $('#documentos_c').attr('class','alert alert-danger');
            //    $("#id_p_nombre_d_o").focus();
            //    return false;
            //}
            //else if ($("#id_p_apellido_d_o").val() == ""){
            //    alert("¿Ingrese el primer apellido en Documentos para conducir");
            //    $('#datos_h').attr('class','alert');
            //    $('#datos_s').attr('class','alert');
            //    $('#documentos_c').attr('class','alert alert-danger');
            //    $("#id_p_apellido_d_o").focus();
            //    return false;
            //}
            //else if ($("#id_direccion_d_o").val() == ""){
            //    alert("¿Ingrese la dirección en Documentos para conducir");
            //    $('#datos_h').attr('class','alert');
            //    $('#datos_s').attr('class','alert');
            //    $('#documentos_c').attr('class','alert alert-danger');
            //    $("#id_direccion_d_o").focus();
            //    return false;
            //}
            else if ($("#id_traspaso").val() == ""){
                apprise("¿Posee traspaso? en Documentos para conducir");
                $('#datos_h').attr('class','alert');
                $('#datos_s').attr('class','alert');
                $('#documentos_c').attr('class','alert alert-danger');
                $("#id_traspaso").focus();
                return false;
            }
            /*else if ($("#id_nom_linea_gren").val() == ""){
                alert("Seleccione el nombre de la linea en Datos de la linea");
                $('#datos_h').attr('class','alert');
                $('#datos_s').attr('class','alert');
                $('#documentos_c').attr('class','alert');
                $('#datos_linea').attr('class','alert alert-danger');
                $("#id_nom_linea_gren").focus();
                return false;
            }*/
        });
        
        // Validacion para la busqueda si un agremiado ya existe en la ficha
        $('#id_status').change(function(){
            cedula = $("#id_cedula_gren").val();
            if (cedula!=0) {
            
                $.get('/registro/ajax_ced_agremiado/', {'cedula':cedula}, function(data) {
                    
                    $.each(data, function(i) {
                        apprise("Disculpe, ya se encuentra registrado el agremiado...");
                        $("#id_cedula_gren").val('').focus();
                        $('#id_sexo').val('');
                        $('#id_status').val('');
                        $("#id_c_agremiado").val('');
                        $("#id_p_nombre").val('');
                        $("#id_s_nombre").val('');
                        $("#id_p_apellido").val('');
                        $('#id_s_apellido').val('');
                        $('#id_fecha_nac').val('');
                        $('#id_edad').val('');
                        $('#id_ins_cne').val('');
                    });
                });
            }
            
            
        });
        
    
    
    $('#id_envio').click(function () {
        if ($("#id_telefonos").val() == "") {
            apprise("Disculpe debe seleccionar los contactos en la lista de envios...");
            $("#id_telefonos").focus();
            return false
        }
        else if ($("#sms_l").val() == "") {
	     apprise('Debe seleccionar una opción en la lista');
	     return false
	} else if ($("#id_sms").val() == "") {
            apprise("Disculpe debe indicar el mensaje a enviar...");
            $("#id_sms").focus();
            return false
        } else {
            apprise("Se ha enviado el mensaje...");

        }
    });


    $('#id_fecha_nac').change(function () {

        fecha_nac = $("#id_fecha_nac").val();

        var fechaActual = new Date()
        var diaActual = fechaActual.getDate();
        var mmActual = fechaActual.getMonth() + 1;
        var yyyyActual = fechaActual.getFullYear();
        
        FechaNac = fecha_nac.split("/");
        var diaCumple = FechaNac[0];
        var mmCumple = FechaNac[1];
        var yyyyCumple = FechaNac[2];
        //alert("DIA: "+diaCumple);
        //retiramos el primer cero de la izquierda
        if (mmCumple.substr(0,1) == 0) {
            mmCumple= mmCumple.substring(1, 2);
        }
        //retiramos el primer cero de la izquierda
        if (diaCumple.substr(0, 1) == 0) {
            diaCumple = diaCumple.substring(1, 2);
        }
        var edad = yyyyActual - yyyyCumple;
        
        /*validamos si el mes de cumpleaños es menor al actual
        o si el mes de cumpleaños es igual al actual
        y el dia actual es menor al del nacimiento
        De ser asi, se resta un año*/
        if ((mmActual < mmCumple) || (mmActual == mmCumple && diaActual < diaCumple)) {
        edad--;
        }
        $("#id_edad").val(edad);
    });

    
});

function PreviewImage_add() {
        var oFReader = new FileReader();
        oFReader.readAsDataURL(document.getElementById("id_foto_add").files[0]);

        oFReader.onload = function (oFREvent) {
            document.getElementById("uploadPreview_add").src = oFREvent.target.result;
        };
    };

function PreviewImage_edit() {
    var oFReader = new FileReader();
    oFReader.readAsDataURL(document.getElementById("id_foto_edit").files[0]);

    oFReader.onload = function (oFREvent) {
        document.getElementById("uploadPreview_edit").src = oFREvent.target.result;
    };
};



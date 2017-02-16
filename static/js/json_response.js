// Funcion 
$(document).ready(function() { // Apertura del ready
	$('#username').focus()
	
////////////////////////////////////////////////////////////////////////////////////////////////////////
// Al cambiar de opción en el combo de estado
////////////////////////////////////////////////////////////////////////////////////////////////////////
$('#id_cod_estado').change(function() {
	var id_est = $('#id_cod_estado').val();
	$('#id_cod_municipio').find('option:gt(0)').remove().end();
	if (id_est > 0) {
	    $.get('/parroquia/busqueda_ajax/', {'id':id_est}, function(data) {
		var option = "";
		$.each(data, function(i) {
		    option += "<option value=" + data[i].fields.cod_municipio + ">" + data[i].fields.municipio + "</option>";
		});
		$('#id_cod_municipio').append(option);
	    }, 'json');
	}
	
	buscar_directivo();
	
});
////////////////////////////////////////////////////////////////////////////////////////////////////////
// Al cambiar de option en el combo municipio
////////////////////////////////////////////////////////////////////////////////////////////////////////
$('#id_cod_municipio').change(function() {
	var id_est  = $('#id_cod_estado').val();
	var id_mun  = $("#id_cod_municipio").val();
	var id_parr = $('#id_cod_parroquia').val();
	
	$('#id_cod_parroquia').find('option:gt(0)').remove().end();
	if (id_est > 0 && id_mun > 0) {
		
	    $.get('/parroquia/busqueda_ajax2/', {'id_est':id_est,'id_mun':id_mun}, function(data) {
		var option = "";
		$.each(data, function(i) {
		    option += "<option value=" + data[i].fields.cod_parroquia + ">" + data[i].fields.parroquia + "</option>";
		});
		$('#id_cod_parroquia').append(option);
	
	    }, 'json');
	}
	
	buscar_directivo();
	
});
////////////////////////////////////////////////////////////////////////////////////////////////////////
//
////////////////////////////////////////////////////////////////////////////////////////////////////////
$('#id_cod_parroquia').change(function(){
	var e = $('#id_cod_estado').val();
	var m = $('#id_cod_municipio').val();
	var p = $('#id_cod_parroquia').val();
	$('#id_cod_n').val(e+''+m+''+p);
});
////////////////////////////////////////////////////////////////////////////////////////////////////////
// Funcion para generar un código de circuito
////////////////////////////////////////////////////////////////////////////////////////////////////////
$('#id_estado').change(function(){
	if ($('#id_estado').val() != 0 && $('#id_codigo_gen').val() != '') {
		var cod_estado = $('#id_estado').val();
		var cod_circuito = $('#id_codigo_gen').val()
		//alert('Estado: '+cod_estado+' - Circuito: '+cod_circuito)
		$('#id_codigo').val(cod_estado+cod_circuito)
	}
});
////////////////////////////////////////////////////////////////////////////////////////////////////////

// Evento para reflejar la carga familiar segun el numero de cedula del gremiado
$("#buscar_c_f").change(function(){
	id_gren = $("#buscar_c_f").val()
	
	if (id_gren > 0) {
		
	    $.get('/registro/ajax_carga_familiar/', {'id_gren':id_gren,}, function(data) {

		var option = "";
		
		if (data.length != 0){
			
			option +="<table class='table' style='width:60em;text-align:center;'>";
				option +="<tr>";
        			option +="<td>";
          				option +='<a href="/carga_familiar/registrar_familiar" title="Nuevo">Agregar carga familiar</a>';
        			option +="</td>";
        			option +="<td><input class='form-control' type='text' id='buscar_c_f' placeholder='Buscar' style='width:110px;' maxlength='9'></td>";
      			option +="</tr>";
				option +="<tr style='background-color: #D9EDF7;'>";
					option +="<td>Cédula</td>";
					option +="<td>Nombres y apellidos</td>";
					option +="<td>Parentesco</td>";
					option +="<td>Edad</td>";
					option +="<td>Discapacidad</td>";
					option +="<td colspan='2'>Acción</td>";
				option +="</tr>";
			$.each(data, function(i) {

				if (data[i].fields.parentesco == 'C') {
					parentesco = 'Cónyuge';
				}
				else if (data[i].fields.parentesco == 'H') {
					parentesco = 'Hijo(a)';
				}if (data[i].fields.edad == 1) {
					edad = data[i].fields.edad+" Año";
				}else{
					edad = data[i].fields.edad+" Años";
				}if (data[i].fields.discapacidad == 'S'){
					discapacidad = 'Sí';
				}else{
					discapacidad = 'No';
				}

				option +="<tr>";
				   option +="<td>"+data[i].fields.cedula+"</td>";
				   option +="<td>"+data[i].fields.nombre+" "+data[i].fields.apellido+"</td>";
				   option +="<td>"+parentesco+"</td>";
				   option +="<td>"+edad+"</td>";
				   option +="<td>"+discapacidad+"</td>";
				   option +="<td>";
					   option +="<a href='/carga_familiar/actualizar_familiar/"+data[i].pk+"'>";
					   		option +="<img src='../../../static/admin/img/icon_changelink.gif' title='Editar'>";
					   option +="</a>";
				   option +="</td>";
				   option +="<td>";
					   option +='<a onclick="eliminar_data_carga_f('+data[i].pk+')">';
					   		option +="<img src='../../static/admin/img/icon_deletelink.gif' title='Eliminar'>";
					   option +="</a>";
				   option +="</td>";
				option +="</tr>";
			});
			
			option +="</table>";
			$('#data_f').html("");
			$('#cargar_data_f').append(option);

		}else{
			alert("Sin registros...");
			$("#buscar_c_f").val("");
			$("#buscar_c_f").focus();
		}
	
	    }, 'json');
	}
});




////////////////////////////////////////////////////////////////////////////////////////////////////////
}); // Cierre del ready
////////////////////////////////////////////////////////////////////////////////////////////////////////
// Funcion global para depurar
////////////////////////////////////////////////////////////////////////////////////////////////////////
function eliminar_data(pk_id, url) {
  id_data= String(pk_id)
  r = confirm("¿Realmente desea eliminar el registro?!");
  if (r == true) {
      location.href=url+id_data;
  }
};

function eliminar_data_carga_f(pk_id) {
  id_data= String(pk_id)
  r = confirm("¿Realmente desea eliminar el registro?!");
  if (r == true) {
      location.href="/carga_familiar/eliminar_familiar/"+id_data;
  }
};
////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////
// Funcion global para buscar un directivo según un estado y un municipio dados.
////////////////////////////////////////////////////////////////////////////////////////////////////////
function buscar_directivo() {
		var id_est  = $('#id_cod_estado').val();
		var id_mun  = $("#id_cod_municipio").val();
		
		if (id_est != "" && id_mun != "" ){
				//alert("Nada todavía... estado: "+id_est+" municipio: "+id_mun);
				$.get('/directiva/busqueda_directivo/', {'id_est':id_est, 'id_mun':id_mun}, function(data) {
				var nombre_coord = "";
				$.each(data, function(i) {
					nombre_coord = data[i].fields.nombre + " " + data[i].fields.apellido;
				});
				$('#id_coordinador').val(nombre_coord);
				}, 'json');
		}else{
				$('#id_coordinador').val("");
		}
};
////////////////////////////////////////////////////////////////////////////////////////////////////////

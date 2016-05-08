/* funcion para la seleccion dinamica en la seccion Direccion del formulario de registro Parroquia*/

function populate(s1,s2){
	var s1 = document.getElementById(s1);
	var s2 = document.getElementById(s2);
	s2.innerHTML = "";
	if(s1.value == "CZP"){
		var optionArray = ["|","barrancas|Barrancas","socorro|Socorro","masparrito|Masparrito"];
	} else if(s1.value == "Dodge"){
		var optionArray = ["|","avenger|Avenger","challenger|Challenger","charger|Charger"];
	} else if(s1.value == "Ford"){
		var optionArray = ["|","mustang|Mustang","shelby|Shelby"];
	}
	for(var option in optionArray){
		var pair = optionArray[option].split("|");
		var newOption = document.createElement("option");
		newOption.value = pair[0];
		newOption.innerHTML = pair[1];
		s2.options.add(newOption);
	}
}
/* funcion para la seleccion dinamica en la seccion Direccion del formulario de registro Barrios*/
function populate2(s1,s2){
	var s1 = document.getElementById(s1);
	var s2 = document.getElementById(s2);
	s2.innerHTML = "";
	if(s1.value == "barrancas"){
		var optionArray = ["|","12demarzo|12 de Marzo","12deoctubre|12 de Octubre","2dediciembre|2 de Diciembre",
		"beltranlucena|Beltran Lucena","buenaventura|Buena Ventura","buenavista|Buena Vista","chicotoro|Chico Toro",
		"conticinio|Conticinio","elcentro|El Cento","elmercadito|El Mercadito","elnazareno|El Nazareno","elretruque|El Retruque",
		"lasesmeraldas|Las Esmeraldas","lamanga|La Manga","lastrinitarias|Las trinitarias","libertador|Libertador",
		"barrionuevo|Barrio Nuevo","puebloviejo|Pueblo Viejo","romulobetancourt|Romulo Betancourt","valleverde|Valle Verde",
		"caseriocampoalegre|Cacerio Campo Alegre","caceriocruzblanca|Cacerio Cruz Blanca","caceriolasguayabitas|Cacerio Las Guayabitas",
		"caceriolosmangos|Cacerio Los Mangos","caceriolosmereyes|Cacerio Los Mereyes","caceriomasparro|Cacerio Masparro",
		"centrobarrancas|Centro Barrancas","sectoraguablanca|Sector Agua Blanca","sectorelalgarrobo|Sector El Algarrobo",
		"sectoreucalipto|Sector Eucalipto","sectormatademango|Sector Mata de Mango","sectormelenero|Sector Melenero","sectorsanrafael|Sector San Rafael",
		"sectorsoco|Sector Soco","sectortinaja|Sector Tinaja"];
	} else if(s1.value == "Dodge"){
		var optionArray = ["|","avenger|Avenger","challenger|Challenger","charger|Charger"];
	} else if(s1.value == "Ford"){
		var optionArray = ["|","mustang|Mustang","shelby|Shelby"];
	}
	for(var option in optionArray){
		var pair = optionArray[option].split("|");
		var newOption = document.createElement("option");
		newOption.value = pair[0];
		newOption.innerHTML = pair[1];
		s2.options.add(newOption);
	}
}

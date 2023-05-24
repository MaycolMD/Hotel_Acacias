let params = new URLSearchParams(window.location.search);
const fechaInicio = params.get('fechaInicio');
const fechafin = params.get('fechaFin');
const adultos = params.get('adultos');
const niños = params.get('niños');
const bebes = params.get('bebes');
const hab = params.get('habitaciones')
const tipo = params.get('tipo');

import API from "./API.js";


const renderGuest = (n) => {
    return `
    <label for="nombre-${n}">Nombre:</label>
    <br>
    <input class="input-default"  type="text" id="nombre-${n}" name="nombre" required>
    <br>
    <label for="apellido-${n}">Apellido:</label>
    <br>
    <input class="input-default"  type="text" id="apellido-${n}" name="apellido" required>
    <br>
    <label for="pais-${n}">Nacionalidad:</label>
    <br>
    <select id="pais-${n}" class="input-default" >
        <option value="Afganistán">Afganistán</option>
        <option value="Albania">Albania</option>
        <option value="Alemania">Alemania</option>
        <option value="Andorra">Andorra</option>
        <option value="Angola">Angola</option>
        <option value="Antigua y Barbuda">Antigua y Barbuda</option>
        <option value="Arabia Saudita">Arabia Saudita</option>
        <option value="Argelia">Argelia</option>
        <option value="Argentina">Argentina</option>
        <option value="Armenia">Armenia</option>
        <option value="Australia">Australia</option>
        <option value="Austria">Austria</option>
        <option value="Azerbaiyán">Azerbaiyán</option>
        <option value="Bahamas">Bahamas</option>
        <option value="Bangladés">Bangladés</option>
        <option value="Barbados">Barbados</option>
        <option value="Baréin">Baréin</option>
        <option value="Bélgica">Bélgica</option>
        <option value="Belice">Belice</option>
        <option value="Benín">Benín</option>
        <option value="Bielorrusia">Bielorrusia</option>
        <option value="Birmania/Myanmar">Birmania/Myanmar</option>
        <option value="Bolivia">Bolivia</option>
        <option value="Bosnia y Herzegovina">Bosnia y Herzegovina</option>
        <option value="Botsuana">Botsuana</option>
        <option value="Brasil">Brasil</option>
        <option value="Brunéi">Brunéi</option>
        <option value="Bulgaria">Bulgaria</option>
        <option value="Burkina Faso">Burkina Faso</option>
        <option value="Burundi">Burundi</option>
        <option value="Bután">Bután</option>
        <option value="Cabo Verde">Cabo Verde</option>
        <option value="Camboya">Camboya</option>
        <option value="Camerún">Camerún</option>
        <option value="Canadá">Canadá</option>
        <option value="Catar">Catar</option>
        <option value="Chad">Chad</option>
        <option value="Chile">Chile</option>
        <option value="China">China</option>
        <option value="Chipre">Chipre</option>
        <option value="Ciudad del Vaticano">Ciudad del Vaticano</option>
        <option value="Colombia">Colombia</option>
        <option value="Comoras">Comoras</option>
        <option value="Corea del Norte">Corea del Norte</option>
        <option value="Corea del Sur">Corea del Sur</option>
        <option value="Costa de Marfil">Costa de Marfil</option>
        <option value="Costa Rica">Costa Rica</option>
        <option value="Croacia">Croacia</option>
        <option value="Cuba">Cuba</option>
        <option value="Dinamarca">Dinamarca</option>
        <option value="Dominica">Dominica</option>
        <option value="Ecuador">Ecuador</option>
        <option value="Egipto">Egipto</option>
        <option value="El Salvador">El Salvador</option>
        <option value="Emiratos Árabes Unidos">Emiratos Árabes Unidos</option>
        <option value="Eritrea">Eritrea</option>
        <option value="Eslovaquia">Eslovaquia</option>
        <option value="Eslovenia">Eslovenia</option>
        <option value="España">España</option>
        <option value="Estados Unidos">Estados Unidos</option>
        <option value="Estonia">Estonia</option>
        <option value="Etiopía">Etiopía</option>
        <option value="Filipinas">Filipinas</option>
        <option value="Finlandia">Finlandia</option>
        <option value="Fiyi">Fiyi</option>
        <option value="Francia">Francia</option>
        <option value="Gabón">Gabón</option>
        <option value="Gambia">Gambia</option>
        <option value="Georgia">Georgia</option>
        <option value="Ghana">Ghana</option>
        <option value="Granada">Granada</option>
        <option value="Grecia">Grecia</option>
        <option value="Guatemala">Guatemala</option>
        <option value="Guyana">Guyana</option>
        <option value="Guinea">Guinea</option>
        <option value="Guinea ecuatorial">Guinea ecuatorial</option>
        <option value="Guinea-Bisáu">Guinea-Bisáu</option>
        <option value="Haití">Haití</option>
        <option value="Honduras">Honduras</option>
        <option value="Hungría">Hungría</option>
        <option value="India">India</option>
        <option value="Indonesia">Indonesia</option>
        <option value="Irak">Irak</option>
        <option value="Irán">Irán</option>
        <option value="Irlanda">Irlanda</option>
        <option value="Islandia">Islandia</option>
        <option value="Islas Marshall">Islas Marshall</option>
        <option value="Islas Salomón">Islas Salomón</option>
        <option value="Israel">Israel</option>
        <option value="Italia">Italia</option>
        <option value="Jamaica">Jamaica</option>
        <option value="Japón">Japón</option>
        <option value="Jordania">Jordania</option>
        <option value="Kazajistán">Kazajistán</option>
        <option value="Kenia">Kenia</option>
        <option value="Kirguistán">Kirguistán</option>
        <option value="Kiribati">Kiribati</option>
        <option value="Kuwait">Kuwait</option>
        <option value="Laos">Laos</option>
        <option value="Lesoto">Lesoto</option>
        <option value="Letonia">Letonia</option>
        <option value="Líbano">Líbano</option>
        <option value="Liberia">Liberia</option>
        <option value="Libia">Libia</option>
        <option value="Liechtenstein">Liechtenstein</option>
        <option value="Lituania">Lituania</option>
        <option value="Luxemburgo">Luxemburgo</option>
        <option value="Macedonia del Norte">Macedonia del Norte</option>
        <option value="Madagascar">Madagascar</option>
        <option value="Malasia">Malasia</option>
        <option value="Malaui">Malaui</option>
        <option value="Maldivas">Maldivas</option>
        <option value="Malí">Malí</option>
        <option value="Malta">Malta</option>
        <option value="Marruecos">Marruecos</option>
        <option value="Mauricio">Mauricio</option>
        <option value="Mauritania">Mauritania</option>
        <option value="México">México</option>
        <option value="Micronesia">Micronesia</option>
        <option value="Moldavia">Moldavia</option>
        <option value="Mónaco">Mónaco</option>
        <option value="Mongolia">Mongolia</option>
        <option value="Montenegro">Montenegro</option>
        <option value="Mozambique">Mozambique</option>
        <option value="Namibia">Namibia</option>
        <option value="Nauru">Nauru</option>
        <option value="Nepal">Nepal</option>
        <option value="Nicaragua">Nicaragua</option>
        <option value="Níger">Níger</option>
        <option value="Nigeria">Nigeria</option>
        <option value="Noruega">Noruega</option>
        <option value="Nueva Zelanda">Nueva Zelanda</option>
        <option value="Omán">Omán</option>
        <option value="Países Bajos">Países Bajos</option>
        <option value="Pakistán">Pakistán</option>
        <option value="Palaos">Palaos</option>
        <option value="Panamá">Panamá</option>
        <option value="Papúa Nueva Guinea">Papúa Nueva Guinea</option>
        <option value="Paraguay">Paraguay</option>
        <option value="Perú">Perú</option>
        <option value="Polonia">Polonia</option>
        <option value="Portugal">Portugal</option>
        <option value="Reino Unido">Reino Unido</option>
        <option value="República Centroafricana">República Centroafricana</option>
        <option value="República Checa">República Checa</option>
        <option value="República del Congo">República del Congo</option>
        <option value="República Democrática del Congo">República Democrática del Congo</option>
        <option value="República Dominicana">República Dominicana</option>
        <option value="República Sudafricana">República Sudafricana</option>
        <option value="Ruanda">Ruanda</option>
        <option value="Rumanía">Rumanía</option>
        <option value="Rusia">Rusia</option>
        <option value="Samoa">Samoa</option>
        <option value="San Cristóbal y Nieves">San Cristóbal y Nieves</option>
        <option value="San Marino">San Marino</option>
        <option value="San Vicente y las Granadinas">San Vicente y las Granadinas</option>
        <option value="Santa Lucía">Santa Lucía</option>
        <option value="Santo Tomé y Príncipe">Santo Tomé y Príncipe</option>
        <option value="Senegal">Senegal</option>
        <option value="Serbia">Serbia</option>
        <option value="Seychelles">Seychelles</option>
        <option value="Sierra Leona">Sierra Leona</option>
        <option value="Singapur">Singapur</option>
        <option value="Siria">Siria</option>
        <option value="Somalia">Somalia</option>
        <option value="Sri Lanka">Sri Lanka</option>
        <option value="Suazilandia">Suazilandia</option>
        <option value="Sudán">Sudán</option>
        <option value="Sudán del Sur">Sudán del Sur</option>
        <option value="Suecia">Suecia</option>
        <option value="Suiza">Suiza</option>
        <option value="Surinam">Surinam</option>
        <option value="Tailandia">Tailandia</option>
        <option value="Tanzania">Tanzania</option>
        <option value="Tayikistán">Tayikistán</option>
        <option value="Timor Oriental">Timor Oriental</option>
        <option value="Togo">Togo</option>
        <option value="Tonga">Tonga</option>
        <option value="Trinidad y Tobago">Trinidad y Tobago</option>
        <option value="Túnez">Túnez</option>
        <option value="Turkmenistán">Turkmenistán</option>
        <option value="Turquía">Turquía</option>
        <option value="Tuvalu">Tuvalu</option>
        <option value="Ucrania">Ucrania</option>
        <option value="Uganda">Uganda</option>
        <option value="Uruguay">Uruguay</option>
        <option value="Uzbekistán">Uzbekistán</option>
        <option value="Vanuatu">Vanuatu</option>
        <option value="Venezuela">Venezuela</option>
        <option value="Vietnam">Vietnam</option>
        <option value="Yemen">Yemen</option>
        <option value="Yibuti">Yibuti</option>
        <option value="Zambia">Zambia</option>
        <option value="Zimbabue">Zimbabue</option>
    </select>
    <br>
    <label for="origen-${n}">Origen:</label>
    <br>
    <input class="input-default"  type="text" id="origen-${n}" name="origen" required>
    <label for="identificacion-${n}">Identificacion (Cedula, número de pasaporte, etc..)</label>
    <input class="input-default"  type="number" style="width: calc(100% - 20px);';"id="identificacion-${n}" name="origen" required>
    `
}
const renderAccordion = (guest, n) => {
    return `
    <button class="accordion">Información del huesped #${n}</button>
    <div class='panel'>
        ${guest}
    </div>
    `
}
window.onload = () => {
    const getGuestNum = parseInt(adultos) + parseInt(niños) + parseInt(bebes);
    console.log(getGuestNum)
    for (let index = 0; index < getGuestNum; index++) {
        let guest = renderGuest(index+1)
        document.querySelector("#guests").innerHTML += renderAccordion(guest, index+1)
    }
    setAccordions()
}
document.querySelectorAll("button.button-default")[1].addEventListener('click', (e) => {
    alert("hola")
    const api = new API();
    let id = 0
    const guestNum = parseInt(adultos) + parseInt(niños) + parseInt(bebes);
    api.assignID(fechaInicio,fechafin,tipo).then((data) => {
        id = data.content.id[0]
        console.log(id)
        for (let index = 0; index < guestNum; index++) {
            const fields = ['nombres-'+(index+1),'apellido-'+(index+1),'pais-'+(index+1),'origen-'+(index+1),'identificacion-'+(index+1)]
            api.reservar(tipo,fechaInicio,fechafin,hab,fields[4], id,fields[2],fields[3],fields[0],fields[1]).then((data)=>{
                if(data.response=="ok") {
                    alert("reservado")
                }
            })
        }
    })
    e.preventDefault();
})
const setAccordions = () => {
    var acc = document.getElementsByClassName("accordion");
    var i;

    for (i = 0; i < acc.length; i++) {
        acc[i].addEventListener("click", function () {
            this.classList.toggle("active");
            var panel = this.nextElementSibling;
            if (panel.style.display === "block") {
                panel.style.display = "none";
            } else {
                panel.style.display = "block";
            }
        });
    }
}
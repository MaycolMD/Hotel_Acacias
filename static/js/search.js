import API from "./API.js";
const roomCardTemplate = (tipo, desc, precio) => {
    return `
    <div class="room-card">
    <div class="room-card-section1">
        <img src="static/assets/Junior-suite.jpg" alt="" srcset="">
    </div>
    <div class="room-card-section2">
        <h1>${tipo}</h1>
        <p>${desc}</p>
        <button class="button-default">Reservar</button>
    </div>
    <div class="room-card-section3">
        <span>${precio}</span>
    </div>
</div>
    `
}
const syncWithMobile = () => {
    //Sync dates with mobile-only reservation inout
    document.getElementById('start-date-mobile').value = document.getElementById('start-date').value
    document.getElementById('end-date-mobile').value = document.getElementById('end-date').value
}
window.onload = () => {
    let params = new URLSearchParams(window.location.search);
    const tipo = params.get('tipo');
    const fechaInicio = params.get('fechaInicio');
    const fechafin = params.get('fechaFin');
    const adultos = params.get('adultos');
    const niños = params.get('niños');
    const bebes = params.get('bebes');
    const hab = params.get('habitaciones')
    const api = new API();
    api.getHabitaciones(tipo, fechaInicio, fechafin, adultos, niños, bebes, hab).then((data) =>
        data.content.forEach(element => {
            console.log(element)
            document.querySelector(".wrapper").innerHTML += roomCardTemplate(element.tipo, element.desc, element.precio)
        })
    )
    document.getElementById('start-date').value = fechaInicio;
    document.getElementById('end-date').value = fechafin;
    document.getElementById('rooms').innerHTML = hab;
    document.getElementById('ocp').innerHTML = `${adultos}-${niños}-${bebes}`
    syncWithMobile()
}
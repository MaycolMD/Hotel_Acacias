const showButton = document.getElementById('ocp');
const favDialog = document.getElementById('occupients');
const rooms = document.getElementById("rooms");
// "Show the dialog" button opens the <dialog> modally
showButton.addEventListener('click', () => {
    favDialog.showModal();
});
rooms.addEventListener('click', () => {
    favDialog.showModal();
});

document.getElementById('ocp-mobile').addEventListener('click', () => {
    favDialog.showModal();
});
document.getElementById('rooms-mobile').addEventListener('click', () => {
    favDialog.showModal();
});
//Sync dates with mobile-only reservation inout
document.getElementById('start-date').addEventListener('change', () => {
    document.getElementById('start-date-mobile').value = document.getElementById('start-date').value
})
document.getElementById('end-date').addEventListener('change', () => {
    document.getElementById('end-date-mobile').value = document.getElementById('end-date').value
})
// 
document.getElementById('start-date-mobile').addEventListener('change', () => {
    document.getElementById('start-date').value = document.getElementById('start-date-mobile').value
})
document.getElementById('end-date-mobile').addEventListener('change', () => {
    document.getElementById('end-date').value = document.getElementById('end-date-mobile').value
})

// "Confirm" button triggers "close" on dialog because of [method="dialog"]
favDialog.addEventListener('close', (e) => {
    document.querySelector("#rooms").innerHTML = document.querySelector("#num-hab").value
    showButton.innerHTML = document.querySelector('#num-adults').value+"-"+document.querySelector('#num-kids').value+'-'+document.querySelector('#num-babies').value
    // mobile controls
    document.querySelector("#rooms-mobile").innerHTML = document.querySelector("#num-hab").value
    document.getElementById('ocp-mobile').innerHTML = document.querySelector('#num-adults').value+"-"+document.querySelector('#num-kids').value+'-'+document.querySelector('#num-babies').value
});

document.querySelector("#num-hab").addEventListener('change', (e)=> {
    document.querySelector("#num-adults").value = document.querySelector("#num-hab").value
    document.querySelector("#num-kids").value = 0
    document.querySelector("#num-babies").value = 0
})
var className = "inverted";
var scrollTrigger = 60;

window.onscroll = function() {
  // We add pageYOffset for compatibility with IE.
  if (window.scrollY >= scrollTrigger || window.pageYOffset >= scrollTrigger) {
    document.getElementsByTagName("header")[0].classList.add(className);
  } else {
    document.getElementsByTagName("header")[0].classList.remove(className);
  }
};
// search bar desktop
document.querySelector('.reservation-bar').querySelector('button').addEventListener('click', (e)=> {
    const startDate = document.querySelector('#start-date').value;
    const endDate = document.querySelector('#end-date').value;
    const hab = document.querySelector('#num-hab').value;
    const adults = document.querySelector('#num-adults').value;
    const kids = document.querySelector('#num-kids').value;
    const babies = document.querySelector('#num-babies').value;
    const type = 'Seleccionar tipo';
    // build str so the button works
    const dir = `search?tipo=${type}&fechaInicio=${startDate}&fechaFin=${endDate}&adultos=${adults}&niños=${kids}&bebes=${babies}&habitaciones=${hab}`
    window.location = dir;
})

  




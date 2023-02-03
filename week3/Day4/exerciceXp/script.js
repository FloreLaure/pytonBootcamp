let sidebar = document.getElementById('sidebar')
//console.log(sidebar);

// bouton pour effacer
let btn = document.createElement('button');
btn.setAttribute('id', 'button')
btn.innerHTML = 'Clear';

btn.addEventListener('click', clear) // onclick évènement 

sidebar.appendChild(btn);

let colors = ['red', 'orange', 'yellow', '#818000', 'gray', 'green', '#3f8', 'cyan', 'blue', 'indigo', 'violet', 'pink', '#3359f8', 'white', 'black',]

for (let i = 0; i < colors.length; i++){
    let newDiv = document.createElement('div');
    newDiv.className = 'color';
    newDiv.addEventListener('click', choose) // évènement pour permettre l'exécution de la fonction quand on choisi la couleur
    newDiv.style.backgroundColor = colors[i];
    sidebar.appendChild(newDiv)
}
let colorSafe = null;//contient la couleur choisie

function choose (event){
    colorSafe = event.target.style.backgroundColor;
}

// éléments où dessiner
let colorgrid = document.getElementById('colorgrid')

for (let i = 0; i < 6000 ; i++){
    let newDiv = document.createElement('div');
    colorgrid.appendChild(newDiv)
    newDiv.className = 'grid';
    newDiv.addEventListener('mousedown', paint)//paint au click
    newDiv.addEventListener('mouseover', paintdrag)// mouseover paint au survol
}

let mousedown = false;
let clearUp = document.getElementById('button');
let grid_fills = document.querySelectorAll('#colorgrid > div');
let body = document.getElementsByTagName('body')[0];

clearUp.addEventListener("click", clear); // clears the creen by clicking the button and calling the function bellow

function clear () {
    for (grid_fill of grid_fills) {
        grid_fill.style.backgroundColor = "white";
    }
    colorSafe = null
}

// vérifie si on a cliqué sur la souris
body.addEventListener("mousedown", function(){
    mousedown = true;
}); 

body.addEventListener("mouseup", function(){
    mousedown = false;
}); 


function paint (event){
   if(colorSafe!=null ){
     event.target.style.backgroundColor = colorSafe;
   }
}
//paint l'arriere plan si on a cliqué sur la souris et si une couleur a été choisi
function paintdrag (event){
  console.log(event);
   if (mousedown && colorSafe != null) {
     event.target.style.backgroundColor = colorSafe;
   }
}
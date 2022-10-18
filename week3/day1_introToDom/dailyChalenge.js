let planete=["Mercure", "Vénus", "Terre", "Mars", "Ceres", "Jupiter", "Saturne", "Uranus", "Neptune", "Pluton"]

let div=document.createElement('div')


for(let planet=0;planet<=planete.length;planet++){
document.getElementsByTagName('body')[0].appendChild(div)
div.innerHTML=document.createTextNode(planet)

}





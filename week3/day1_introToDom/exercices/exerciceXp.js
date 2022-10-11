//  exercice 1

//1
let div_value=document.getElementById("container").innerHTML
console.log(div_value)

//2
let lis=document.getElementsByTagName('li')
for(let i=0;i<lis.length;i++){
	if (lis[i].innerHTML=="Pete"){
		lis[i].innerHTML="Richard"
	}
}
//3
for(let i=0;i<lis.length;i++){
	lis[i].innerHTML="Kévine"
}

//4
let uls=document.getElementsByTagName('ul')
for(let i=0;i<lis.length;i++){
	if (lis[i].innerHTML=="Sarah"){
		uls[1].removeChild(lis[i])
	}
}




//  exercice 2

//2

document.getElementsByTagName('div')[0].style.backgroundColor='#33ccff'

document.getElementsByTagName('div')[0].style.padding='5px'

//3
let lis=document.getElementsByTagName('li')
document.getElementsByTagName('ul')[0].removeChild(lis[0])


// 4
document.getElementsByTagName('li')[0].style.border='2px solid black'

// 5

document.getElementsByTagName('body')[0].style.fontSize='25px'




// exercice 3

// 2

let A=document.getElementById('navBar')
A.setAttribute('id','socialNetworkNavigation')
console.log(A)

// 3

//1

let newLi=document.createElement('li')

// 2
let noeud=document.createTextNode("Logout")

// 3

newLi.appendChild(noeud)

// 4

let C=document.getElementById('socialNetworkNavigation').children[0]
C.appendChild(newLi)

//let C=document.getElementById('socialNetworkNavigation').firstElementChild

//document.getElementsByTagName('ul')[2].appendChild(newLi)



// exercice 4

let allBooks=[
	{
		title:"Candide",
		author:"Voltaire",
		image :"https://img.lemde.fr/2019/04/15/0/0/3117/4003/664/0/75/0/23318c2_kk2T57UaTf1581M8X6RIH0_C.jpg",
		alreadyRead : true
	},

	{
		title:"Le monde s'éfondre",
		author:"Chinua Achebe",
		image :"https://img.chasse-aux-livres.fr/v7/_am1_/41OMRli4nQL.jpg?w=1200&h=1200&func=bound&org_if_sml=1",
		alreadyRead : false
	}
]

// Creation de l'element table

let table=document.createElement('table')

// Creation des elements th  d'entete du tableau
let head1=document.createElement('th')
let head2=document.createElement('th')
let head3=document.createElement('th')

// Creation des elements tr des ligne du tableau
let ligne1=document.createElement('tr')
let ligne2=document.createElement('tr')
let ligne3=document.createElement('tr')

// Creation des elements td des colonnes du tableau
let colone1=document.createElement('td')
let colone2=document.createElement('td')
let colone3=document.createElement('td')
let colone4=document.createElement('td')
let colone5=document.createElement('td')
let colone6=document.createElement('td')

// Creation des elements img pour les images

//let img1=document.createElement('img')
//let img2=document.createElement('img')
const img1 = new Image(80, 80);
const img2 = new Image(80, 80);


// Creation des elements titre des entetes
let titre=document.createTextNode("title")
let auteur=document.createTextNode("author")
let image=document.createTextNode("image")

//ajout du tableau au document html
document.getElementsByClassName('listBooks')[0].appendChild(table)

//ajout des celules des entetes de la ligne 1 du tableau
ligne1.appendChild(head1)
ligne1.appendChild(head2)
ligne1.appendChild(head3)

//ajout des valeurs des entetes 
head1.appendChild(titre)
head2.appendChild(auteur)
head3.appendChild(image)

//ajout des colonnes de la ligne 2 du tableau
ligne2.appendChild(colone1)
ligne2.appendChild(colone2)
ligne2.appendChild(colone3)

//ajout de l'element img a la colonne 3 de la ligne 2
colone3.appendChild(img1)

//ajout des valeurs de la premiere ligne de donnees
colone1.innerHTML=allBooks[0].title
colone2.innerHTML=allBooks[0].author
img1.src = allBooks[0].image

//ajout des colonnes de la ligne 3 du tableau
ligne3.appendChild(colone4)
ligne3.appendChild(colone5)
ligne3.appendChild(colone6)

//ajout de l'element img a la colonne 3 de la ligne 3
colone6.appendChild(img2)


//ajout des valeurs de la deuxieme ligne de donnees
colone4.innerHTML=allBooks[1].title
colone5.innerHTML=allBooks[1].author
img2.src = allBooks[1].image

//application de style aux elements
img1.style.borderRadius = '50px'
img2.style.borderRadius = '50px'
table.style.border = '1px solid grey'
colone1.style.border = '1px solid grey'
colone2.style.border = '1px solid grey'
colone3.style.border = '1px solid grey'
colone4.style.border = '1px solid grey'
colone5.style.border = '1px solid grey'
colone6.style.border = '1px solid grey'
head1.style.border = '1px solid grey'
head2.style.border = '1px solid grey'
head3.style.border = '1px solid grey'

//verifie si le livre est lu appliquer le style couleur rouge aux detail du livre
if (allBooks[0].alreadyRead==true){
	colone1.style.color = 'red'
	colone2.style.color = 'red'
}
if (allBooks[1].alreadyRead==true){
	colone4.style.color = 'red'
	colone5.style.color = 'red'
}


//ajout des lignes aux tableau
table.appendChild(ligne1)
table.appendChild(ligne2)
table.appendChild(ligne3)











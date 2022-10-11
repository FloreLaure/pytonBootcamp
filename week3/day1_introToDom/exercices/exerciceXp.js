/*//  exercice 1

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
*/



//  exercice 2

//2
/*
document.getElementsByTagName('div')[0].style.backgroundColor='#33ccff'

document.getElementsByTagName('div')[0].style.padding='5px'

//3
let lis=document.getElementsByTagName('li')
document.getElementsByTagName('ul')[0].removeChild(lis[0])


// 4
document.getElementsByTagName('li')[0].style.border='2px solid black'

// 5

document.getElementsByTagName('body')[0].style.fontSize='25px'

*/


// exercice 3

// 2
/*
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

*/


// exercice 4

let allBooks=[
	{
		title:"Candide",
		author:"Voltaire",
		image :"https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.amazon.com%2FCandide-Voltaire%2Fdp%2F1503253791&psig=AOvVaw1vjwGa2xS9lQXUwKzpFawA&ust=1665333690624000&source=images&cd=vfe&ved=0CAwQjRxqFwoTCLiV5cqJ0foCFQAAAAAdAAAAABAE",
		alreadyRead : true
	},

	{
		title:"Le monde s'éfondre",
		author:"Chinua Achebe",
		image :"https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.amazon.com%2FCandide-Voltaire%2Fdp%2F1503253791&psig=AOvVaw1vjwGa2xS9lQXUwKzpFawA&ust=1665333690624000&source=images&cd=vfe&ved=0CAwQjRxqFwoTCLiV5cqJ0foCFQAAAAAdAAAAABAE",
		alreadyRead : false
	}
]



let table=document.createElement('table')

let head1=document.createElement('th')
let head2=document.createElement('th')
let head3=document.createElement('th')

let ligne1=document.createElement('tr')
let ligne2=document.createElement('tr')
let ligne3=document.createElement('tr')


let colone1=document.createElement('td')
let colone2=document.createElement('td')
let colone3=document.createElement('td')
let colone4=document.createElement('td')
let colone5=document.createElement('td')
let colone6=document.createElement('td')

let img1=document.createElement('img')
let img2=document.createElement('img')



let titre=document.createTextNode("title")
let auteur=document.createTextNode("author")
let image=document.createTextNode("image")

document.getElementsByClassName('listBooks')[0].appendChild(table)

ligne1.appendChild(head1)
ligne1.appendChild(head2)
ligne1.appendChild(head3)

head1.appendChild(titre)
head2.appendChild(auteur)
head3.appendChild(image)




ligne2.appendChild(colone1)
ligne2.appendChild(colone2)
ligne2.appendChild(colone3)

colone1.innerHTML=allBooks[0].title
colone2.innerHTML=allBooks[0].author
colone3.innerHTML=allBooks[0].image


ligne3.appendChild(colone4)
ligne3.appendChild(colone5)
ligne3.appendChild(colone6)

colone4.innerHTML=allBooks[1].title
colone5.innerHTML=allBooks[1].author
colone6.innerHTML=allBooks[1].image



table.appendChild(ligne1)
table.appendChild(ligne2)
table.appendChild(ligne3)













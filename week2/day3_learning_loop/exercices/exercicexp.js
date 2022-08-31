
 //exercice1

let people = ["Greg", "Mary", "Devon", "James"];



	//part1

			//1

people.splice(0,1);

//2

people.splice(2,1,"jason");


//3
people.push("Flore");


//4
console.log(people.indexOf("Mary"));


//5
people.slice(1,4);


//6

console.log(people.indexOf("Foo"));//il renvoi -1 car Foo n'existe pas dans la chaine


	//part2 loop

	let i=0;
	while (i<=people.length){
		console.log(people[i]);
		i=i+1;
	}



	let j=0;
	while (j<=people.length){
		console.log(people[j]);
		j=j+1;
		if (j>2) {
			break;
		};
	}



	//exercice2
	

let colors = ["red", "pink", "blue", "black", "white"];

i=0;
while(i<=4){
	colors.splice(i,1," mon choix "+ (i+1) + " est " + colors[i]);
	i=i+1;
  
}
console.log(colors);


//exercice3 Repeat thr question

k=0;
do{
var typ = prompt("Entrez un numero");
k=k+1;
}
while(typ<10);



//exercice4

//1

let building = {
    numberOfFloors : 4,
    numberOfAptByFloor : {
        firstFloor : 3,
        secondFloor : 4,
        thirdFloor : 9,
        fourthFloor : 2,
    },
    nameOfTenants : ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan :  [4, 1000],
        david : [1, 500],
    },
}

//2

console.log((Object.values(building))[0]);



//3 Console.log how many apartments are on the floors 1 and 3.

console.log((Object.values((Object.values(building))[1]))[0]+" "+(Object.values((Object.values(building))[1]))[2]);




//4 Console.log the name of the second tenant and the number of rooms he has in his apartment. 

console.log(((Object.values(building))[2])[1]+" " + ((Object.values((Object.values(building))[3]))[1])[0]);




//5 Check if the sum of Sarah’s and David’s rent is bigger than Dan’s rent. If it is, than increase Dan’s rent to 1200.

let rentDan = ((Object.values((Object.values(building))[3]))[1])[1];

let sumSaraDavidRent = ((Object.values((Object.values(building))[3]))[0])[1] + ((Object.values((Object.values(building))[3]))[2])[1];

if (sumSaraDavidRent> rentDan) {
	rentDanIncrease=((Object.values((Object.values(building))[3]))[1])[1]+1200;

}



//exercice5 :Family


let family={
	parent:["father","mother"],
	childs:{
		girl:"fatou",
		boy:"ismael",

	},
	friends:["alima","kady","pascal","moussa"],
}


//2
for(let i in family){
	console.log(i);
}


//3
for(let i in family){
	console.log(family[i]);
}



//exercice6



let details = {
  my: 'name',
  is: 'Rudolf',
  the: 'raindeer'
}
let s=" ";
for(let i in details){
	var j=(i);
	var k=(details[i]);
	s=s+(j+" "+k+" ");
}
console.log(s);




//exercice7


let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
let name=names.sort();
let s=""
for (let m in name){
s=s+((name[m])[0]);
}
console.log(s);
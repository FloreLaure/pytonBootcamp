
//learning conditionals

	//exercices xp

		//exercice1

let x=5;
let y=15;
if (x>y) {console.log("x is the biggest number");}
else {console.log("y is the biggest number");}


		//exercice2

const newDog = "Chihuahua";
lon = newDog.length;
console.log("there are "+lon +" letters");
console.log(newDog.toUpperCase());
console.log(newDog.toLowerCase());

if (newDog=="Chihuahua") {console.log("I love Chihuahuas,it's my favorite dog breed");}
else{console.log("I dont care, I prefer cats");}



	//exercice3


	let x=prompt("Entrez un nombre");
	if (x%2==0){
		console.log(x + " is an even number");
	}
	else{
		console.log(x + " is an odd number");
	}



	//exercice4

	let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];
	if (users.length==0){
		console.log("the users array is empty");
	}
	else if(users.length==1){
		console.log(users[0]+ " is online");
	}
	else if(users.length==2){
		console.log(users[0]+ " and " +users[1] + " are online");
	}
	else{
		console.log(users[0] ", " users[1] + " and " +users.length-2 +" more are online");
	}



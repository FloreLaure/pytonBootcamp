
//exercice1

	//part 1
function infoAboutMe(){
	console.log("SAWADOGO Kévine 21 ans");
}

infoAboutMe();



	//part 2

function infoAboutPerson(personName, personAge, personFavoriteColor){
	console.log("your name is "+personName+",you are "+personAge+" year old "+" your favorite color is "+personFavoriteColor);

}

infoAboutPerson("David", 45, "blue");
infoAboutPerson("Josh", 12, "yellow");




//exercice2

function calculateTip() {
	let x=Number(prompt("Entrer le montant de la facture"));
	if (x<50){
		var y=(20*x)/100;
	}
	else if ((x>=50)&&(x<=200)){
		var y=(15*x)/100;
	}
	else{
		var y=(10*x)/100;
	}
	
	console.log("the tip amount and the final bill "+(x+y));
};

calculateTip()



//exercice3

function isDivisible(){
	var j=0;
	for (var i =0; i <=500; i++) {
		if (i%23==0) {
			console.log(i)
			j=j+i;
		}
		
	}
	console.log("sum:"+j);
}


isDivisible();



//exercice4


var stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

var prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 

var shoppingList=["banana", "orange", "apple"]; 

function myBill(){
	for (var i in shoppingList) {

		if (shoppingList[i] in stock) {
			console.log(shoppingList[i]);
		}
	}

myBill();


//Exercice 5 
	//1
	function changeEnough(itemPrice, amountOfChange) {
		let sum = 0;//3
		sum += amountOfChange[0]*0.25;
		sum += amountOfChange[1]*0.10;
		sum += amountOfChange[2]*0.05;
		sum += amountOfChange[3]*0.01;
		if(sum >= itemPrice) {
			return true;//2
		} else {
			return false;
		}
	}
	changeEnough(14.11, [2,100,0,0]);
	changeEnough(0.75, [0,0,20,5]);

//Exercice 6 
	//1
	function hotelCost() {	
		while(1) {
			let nombreNuit = prompt("Combien de nuit souhaitez vous séjourner à l'hotel");
			type = Number(nombreNuit);
			if (!type) {
				console.log("Erreur!!! Entrez un nombre de nuit");
			} else return 140*type;
		}
	}
	//2
	function planeRideCost() {
		while(1) {
			let destination = prompt("Quelle est votre destination ?");
			type = Number(destination);
			if (type) {
				console.log("Erreur!!! Entrez votre destination");
			} else {
				if (destination=="Londres") return 183;
				else if (destination=="Paris") return 220;
				else return 300;
			}
		}
	}
	//3
	function rentalCarcost() {
		while(1) {
			let location = prompt("Combien de jours souhaitez vous louer la voiture");
			type = Number(location);
			if (!type) console.log("Erreur!!! Entrez un chiffre"); 
			else {
				if (type > 10) return 40*type-40*type*0.1;
				else return 40*type;
			}
		}
	}

	//4
	function totalVacationCost() {
		console.log("La voiture coûte : " + rentalCarcost() + ", l'hôtel coûte " + hotelCost() + ", les billets d'avions coûtent " + planeRideCost())
	}
	//5
	totalVacationCost();
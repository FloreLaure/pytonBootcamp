
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


let stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

let prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 

let shoppingList["banana","orange","apple"];
function myBill(){

}

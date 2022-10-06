//Exercice 1 
	let numbers = [123, 8409, 100053, 333333333, 7]
	for (x of numbers) {
		if (x%3 == 0) 
			console.log(x ,": true");
		else 
			console.log(x ,": fasle");
	}

//Exercice 2 
	let guestList = {
		randy: "Germany",
		karla: "France",
		wendy: "Japan",
		norman: "England",
		sam: "Argentina"
	}
	//1
	nom = prompt("Entrez votre nom");
	//2
	if (nom in guestList)
		console.log("Hi! I'm" , nom + ", and I'm from ",guestList[nom]);	
	else
		console.log("Hi! I'm a guest.");

//Exercice 3
	let age = [20,5,12,43,98,55];
	//1
	let sum = 0;
	for(x of age)
		sum += x;
	console.log("La somme de tous les nombres:",sum)
	//2
	let plusGrand = 0;
	for (x of age)
		if (x > plusGrand)
			plusGrand = x;
	console.log("L'âge le plus élevé :",plusGrand,"ans");
//Exercice 1 
	//Premiere partie
	function numberVerif(nombre) {
		type = Number(nombre);
		if (!type) {
			console.log("Désolé, pas un numéro");
			return false;
		} else if (nombre < 0 && nombre > 10){
			console.log("Désolé, ce n'est pas un bon chiffre");
			return false;
		} else {
			return true;
		}
	}

	function aléatoireNum(min,max) {
		min = Math.ceil(min);
		max = Math.floor(max+1);
		let nombre = Math.floor(Math.random()* (max - min)) + min;
		return nombre;
	}

	function playTheGame() {
		let confirmation=confirm("Voulez vous jouer au jeu?")
		if (!confirmation) {//1
			console.log("Pas de problème au revoir");
			return;
		} else {//2
			let userNumber;
			do {
				userNumber = prompt("Entrez un nombre entre 0 et 10","4");
				if (numberVerif(userNumber)) {
					computerNumber = aléatoireNum(0,10);
					compareNumbers(userNumber,computerNumber);
				}
			} while (!numberVerif(userNumber))//prime
		}

	}

	//Deuxieme partie
	function compareNumbers(userNumber,computerNumber) {
		let i=0;
		while(i!=4) {
			if (userNumber == computerNumber) {
				alert("WINNER");
				return;
			} else if (userNumber > computerNumber && i!=3) {
				userNumber = prompt("Votre numéro est plus grand que celui de l'ordinateur, devinez encore"); 
				while(!numberVerif(userNumber))
					userNumber = prompt("Entrez un nombre entre 0 et 10");
			}
			else if (userNumber < computerNumber && i!=3) {
				userNumber = prompt("Votre numéro est plus petit que celui de l'ordinateur, devinez encore"); 
				while(!numberVerif(userNumber))
					userNumber = prompt("Entrez un nombre entre 0 et 10");
			}	
			else if ( i == 3) {
				alert("pas de chances");
				return;
			}
			i++;
		}
	}
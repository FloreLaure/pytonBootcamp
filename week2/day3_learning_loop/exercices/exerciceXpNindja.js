//Exercice 1 
	//1//2
	let personne = [
		{
			nom : "SAWADOGO",
			prenom : "Flore",
			masse : 55,
			taille : 170,
			imc : function () {
				return this.masse/(this.taille*this.taille);
			}
		},
		{
			nom : "Ouedraogo",
			prenom : "Séverine",
			masse : 75,
			taille : 168,
			imc : function () {
				return this.masse/(this.taille*this.taille);
			}
		}
	];
	//3//4
	function compImc(){
		if (personne[0].imc() > personne[1].imc())
			console.log(personne[0].nom, personne[0].prenom , "a le plus grand IMC");
		else
			console.log(personne[1].nom , personne[1].prenom  , "a le plus grand IMC");
	}

	compImc();

//Exercice 2 
	
	function findAvg(gradesList) {
		moyenne = 0;
		for(x of gradesList)
			moyenne += x;
		moyenne = moyenne / gradesList.length
		if (moyenne > 65)
			console.log("Votre moyenne est :",moyenne + ", vous avez réussi.");
		else 
			console.log("Vous avez échouez, try again");		
	}
	findAvg([42,90,86,99,85]);
	
	//Bonus
	function moy(gradesList) {
		sum = 0;
		for(x of gradesList)
			sum += x;
		return sum/gradesList.length;
	}

	function isSuccess(gradesList) {
		moy(gradesList);
		if (moyenne > 65)
			console.log("Votre moyenne est :",moyenne + ", vous avez réussi.");
		else 
			console.log("Vous avez échouez, try again");
	}

	isSuccess([42,90,86,99,85]);
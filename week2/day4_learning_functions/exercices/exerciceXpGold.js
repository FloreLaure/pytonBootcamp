//Exercise 1 
	function isBlank(mot) {
		if (mot == "") return true;
		else return false;
	}

	console.log(isBlank(''));
	console.log(isBlank('abc'));

//Exercice 2 : Abrév_name
	function abbrevName(mot) {
		mot = mot.split(" ");
		motC = mot[0] + " ";
		for (let i = 1; i < mot.length; i++)
			motC += mot[i][0].toUpperCase() + ". ";
		return motC;
	}

	console.log(abbrevName("Robin Singh"));
	console.log(abbrevName("SAWADOGO Laure Flore Kévine"));


//Exercice 3 : SwapCase
	function swapCase (mot) {
		let motC = "";
		for (let i = 0; i <mot.length;i++)
			if (mot[i] == mot[i].toUpperCase()) 
				motC += mot[i].toLowerCase();
			else 
				motC += mot[i].toUpperCase();
		console.log(motC);
	}

	swapCase('The Quick Brown Fox');

//Exercice 4 

function isOmnipresent(tabNumber, Number) {
	for (x of tabNumber) 
		for (y of x)
			if (Number == y) return true;
			else return false;
}

isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 1);
isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 6);
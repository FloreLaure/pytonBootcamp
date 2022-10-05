
79 lines (71 sloc) 1.68 KB
//Exercice 1 
	//1
	let min = Math.ceil(1);
	let max = Math.floor(101);
	let nombre = Math.floor(Math.random()* (max - min)) + min;
	console.log(nombre);
	//2
	let pair= "";
	for ( let i = 1; i <= nombre; i++) 
		if (i%2 == 0 && i < nombre) 
			pair += i + " ";	
	console.log(pair);

//Exercice 2 : Lettres Majuscules
	function capitalize(mot) {
		let motP = "";
		let motI = "";
		for ( let i = 0; i < mot.length; i++)
			if (i%2 == 0)
				motP += mot[i].toUpperCase();
			else
				motP += mot[i];
		for ( let i = 0; i < mot.length; i++)
			if (i%2 != 0)
				motI += mot[i].toUpperCase();
			else
				motI += mot[i];
		let result = [motP,motI];
		return result;
	}

	capitalize("abcdef");

//Exercice 3 
	function palindrome(mot) {
		mot=mot.toLowerCase();
		if (mot.length%2 == 0)
			return false;
		else
			for(let i = 0; i < mot.length; i++)
				if (mot[i] != mot[mot.length-i-1])
						return false;
		return true;
	}

	palindrome("Madam");

//Exercice 4 
	function biggestNumberInArray(arrayNumber) {
		let biggestNumber = 0;
		if (arrayNumber == [])
			return 0;
		for (x of arrayNumber)
			if (Number(x) && x > biggestNumber)
				biggestNumber = x;
		return biggestNumber;
	}

	biggestNumberInArray([-1,0,3,100, 99, 2, 99]);
	biggestNumberInArray(['a', 3, 4, 2]);
	biggestNumberInArray([]);

//Exercice 5 
	function listUniq(tabNumber) {
		let tabNumber1 = [];
		for (x of tabNumber){
			let valide = 0;
			for (y of tabNumber1)
				if (tabNumber1 == [])
					tabNumber1[0]=x;
				else if (x == y)
					valide = 1;
			if (valide==0)
				tabNumber1[tabNumber1.length]=x;
		}
		return tabNumber1;
	}

	listUniq([1,2,3,3,3,3,4,5]);
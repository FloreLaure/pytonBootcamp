function several_words(mots) {
	let longEtoile = 0;
	for (let x of mots)
		if (longEtoile < x.length) 
			longEtoile = x.length;
	return longEtoile;
}

function etoile(longEtoile) {
	let etoile = "*";
	for (var i = longEtoile + 4; i > 1; i--) 
		etoile = etoile + "*";
	return etoile;
}

function afficher(mots) {
	mots = mots.split(",");
	longEtoile=several_words(mots);
	etoile=etoile(longEtoile);
	console.log(etoile);
	for (let x of mots) {
		let mot = "* " + x;
		for (i=mot.length; i < longEtoile+3; i++)
			mot = mot + " ";
		console.log(mot + "*");
	}
	console.log(etoile);
}

afficher(prompt("Entrez plusieurs mots séparés par des virgules"));
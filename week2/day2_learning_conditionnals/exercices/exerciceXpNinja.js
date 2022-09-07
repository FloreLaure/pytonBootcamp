
//exercice 1
let age1=Number(prompt("Entrez votre année de naissance"));

let age2=Number(prompt("Entrez votre année de naissance"));

if (age1<age2){
	console.log((2*age2)-(age1));
}
if (age2<age1) {
	console.log((2*age1)-(age2));

}

//exercice 2

let code=prompt("Entrezvotre code postal");
let code1=Number(code)
if((code.length == 5)&&(code1 != NaN))
{
	console.log("success");
}
else {console.log("error");}



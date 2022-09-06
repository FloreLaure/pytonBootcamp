
//exercice 1

let langue=prompt("Quelle est votre langue?").lowercase

switch(langue) {
  case francais:
    console.log("Bonjour");
    break;
  case anglais:
    console.log("Hello");
    break;
  case hebreux:
    console.log("Shalom");
    break;
  default:
    console.log("01110011"+" 01101111" +"01110010 " +"01110010 "+" 01111001");  
}


//exercice 2

let note=prompt("Entrez votre note");
let note1=Number(note);
if (note1>90) {
  console.log("A");
}
else if ((note1>80) && (note1<=90)) {
  console.log("B");
}
else if ((note1>70) && (note1<=80)) {
  console.log("C");
}  
else{
  console.log("D");
}



//exercice3

var chaine=prompt("Entrer une chaine de carctère").lowercase;
if((chaine.length >=3) && (chaine.endsWith('ing') is (false)))
{

  console.log(chaine.push("ing"));
}


if ((chaine.length >=3)&&(chaine.endsWith('ing'))){
 console.log(chaine.push("ly"))
};
if (chaine.length < 3){
  console.log(chaine);
}
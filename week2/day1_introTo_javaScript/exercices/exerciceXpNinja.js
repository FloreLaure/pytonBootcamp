    
    //exercice 1

    5 >= 1 //True
    0 === 1 //False
    4 <= 1 //False
    1 != 1 // False
    "A" > "B" //False
    "B" < "C" //True
    "a" > "A" //True
    "b" < "A" //false
    true === false //False
    true != true //False




    //exercice 2

    //1
    let nombres = prompt("Entrez deux nombres séparés par une virgule");
    nombres = nombres.split(",");
    console.log("La somme de" , nombres[0] , " et " , nombres[1] , " est " , Number(nombres[0]) + Number(nombres[1]) );

//Exercice 3 
    //1
    let chaine = prompt("Entrez une phrase contenant le mot Nemo");
    //2
    console.log(chaine);
    chaine=chaine.split(" ");
    trouver = chaine.indexOf("Nemo");
    //3
    console.log("Chaine trouvée à la position" , trouver);
    //4
    if (trouver != -1) {
        console.log("Chaine trouvée à la position" , trouver);  
    } else {
        console.log("La chaine n'a pas été trouvé");  
    }

//Exercice 4 : 
    
    let numero = Number(prompt("Entrez un numéro"));
    //2
    let chaine = "b";
    if (numero < 2) {
        chaine = "boum";
        if ((numero%2) == 0){
            console.log("divisible par 2" , chaine + "!");
        } else if ((numero%5) == 0){
            console.log("divisible par 5" , chaine.toUpperCase() + "!");
        } else if ((numero%5) && (numero%2) == 0){
            console.log(chaine.toUpperCase() + "!");
        } else {
            console.log("Ni divisible par 2, ni par 5  ", chaine);
        }
    } else {//si sup. ou égal 2
        for (var i = 1; i <= numero ; i++) {
            chaine=chaine+"o";
        }
        chaine=chaine+"u";
        chaine=chaine+"m";
        if ((numero%2) == 0){
            console.log("divisible par 2" , chaine + "!");
        } else if ((numero%5) == 0){
            console.log("divisible par 5" , chaine.toUpperCase() + "!");
        } else if ((numero%5) && (numero%2) == 0){
            console.log(chaine.toUpperCase() + "!");
        } else {
            console.log("Ni divisible par 2, ni par 5  ", chaine);
        }
    } 


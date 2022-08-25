
//exercice1

let fruits = ["Banana", "Apples", "Oranges", "Blueberries"];

fruits .splice(0,1,);


fruits.sort();


fruits.push("kiwi");

fruits .splice(0,1,);


let inverse=fruits.sort();
inverse.reverse();




//exercice2

let moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
console.log(moreFruits[1,1,0]);
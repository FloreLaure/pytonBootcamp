

//exercice1//

let food="chocolate";
let meal="dinner";
console.log("I eat " +food +" at every " +meal);


					//exercice2//

					//part 1//

let myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];
let myWatchedSeriesLength=myWatchedSeries.length;
let myWatchedSeriesSentence="black mirror, money heist, and the big bang theory";
console.log("j'ai regarder " +myWatchedSeriesLength +" séries: " +myWatchedSeriesSentence);


				//part 2//

//1//
myWatchedSeries.splice(2,1,"friends");

// 2//
myWatchedSeries.push("peaky blinder")


//3//
myWatchedSeries.splice(0,0,"lucifer");


//4//
myWatchedSeries.splice(1,1);


//5//
let x="money heist";
let y= x.split(" ").indexOf(2);
console.log(y);

//6//
console.log(myWatchedSeries);




//exercice3//

let tempsCel=25;
let tempsF=(tempsCel/5*9)+32;
console.log(tempsF);



//exercice4//

    let c;
    let a = 34;
    let b = 21;

    console.log(a+b) //first expression
    // Prediction:  La sortie sera 55 car 34 er 21 sont des nombres et 34+21=55
    // Actual:55


     a = 2;

    console.log(a+b) //second expression
    // Prediction: La sortie sera 23 car la valeur de a a eté changé à 2 et 2+21=23
    // Actual:23


    //La valeur de c n'est pas définit

    console.log(3 + 4 + '5');//la sortie est 75




//exercice5


typeof(15)
// Prediction:number
// Actual:number

typeof(5.5)
// Prediction:number
// Actual:number

typeof(NaN)
// Prediction:string
// Actual:string

typeof("hello")
// Prediction:string
// Actual:string

typeof(true)
// Prediction:Boolean
// Actual:Boolean

typeof(1 != 2)  //1!=2 retourne vrai  qui est un boonean
// Prediction:Boolean
// Actual:Boolean

"hamburger" + "s"  //concatenation de deux srting
// Prediction:hamburgers
// Actual:hamburgers

"hamburgers" - "s" //l'operateur - ne s'applique pas aux string
// Prediction:NAN
// Actual:NAN

"1" + "3" //concatenation de deux srting
// Prediction:13
// Actual:13

"1" - "3" //l'operateur - ne s'applique pas aux string
// Prediction:NAN 
// Actual:-2

"johnny" + 5
// Prediction:johnny5
// Actual:johnny5

"johnny" - 5  //l'operateur - ne s'applique pas sur deux types differents
// Prediction:NAN
// Actual:NAN

99 * "hello"  //l'operateur * ne s'applique pas sur deux types differents
// Prediction:NAN
// Actual:NAN

1 != 1  //1 n'est pas different de 1
// Prediction:false
// Actual:false

1 == "1" //1 est egal à "1" en valeur
// Prediction:true
// Actual:true

1 === "1"  //1 est different de "1" de par leur types
// Prediction:false
// Actual:false



//exercice 6

5 + "34"
// Prediction:534
// Actual:534

5 - "4"
// Prediction:
// Actual:

10 % 5
// Prediction:0
// Actual:0

5 % 10
// Prediction:5
// Actual:5

"Java" + "Script"
// Prediction:JavaScript
// Actual:JavaScript

" " + " "
// Prediction:
// Actual:"  "

" " + 0
// Prediction:" 0" 
// Actual: " 0"

true + true //true= 1 et 1+1=2
// Prediction:2
// Actual:2

true + false //false=0 et 1+0=1
// Prediction:1
// Actual:1

false + true //false=0 et 1+0=1
// Prediction:1
// Actual:1

false - true//0-1=-1
// Prediction:-1
// Actual:-1

!true //contraire de true est false
// Prediction:false
// Actual:false

3 - 4 /3-4=-1
// Prediction:-1
// Actual:-1

"Bob" - "bill"  //l'operateur - ne s'applique pas aux string
// Prediction:NAN
// Actual:NAN



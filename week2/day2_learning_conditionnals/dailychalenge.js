let sentence ="The movie is not that bad, I like it";


//2
let sentences=sentence.split(" ");

let wordNot=3;




//3
let wordBad=5;


//4
if(wordNot < wordBad){
sentences.splice(3,3,"good");
console.log(sentences);
}
else{
	console.log(sentence);
}
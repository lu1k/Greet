let showWord = setInterval(foo, 3000);
let words = ['share', 'care', 'fear'];
let arrLen = words.length;

function foo () {
	let toggleWord = document.querySelector(".mappingText");
	randNum = Math.floor(Math.random() * arrLen);
	toggleWord.innerHTML = words[randNum].toUpperCase();
	console.log(words[randNum].toUpperCase());
}
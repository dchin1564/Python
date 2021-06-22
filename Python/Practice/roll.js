
function CaesarCipher(s, roll) {
    // you can comment this line
    s = s.toLowerCase();
    s = s.split("");
    var result = '';
    var charcode = 0;
    

    for (var i = 0; i < roll.length;i++){
        var num = roll[i];
        for (var j = 0; j < num; j++){
            charcode = (s[j].charCodeAt())+1;
            if (s[j].charCodeAt() == 122){
                charcode = 97;
            }
            result = String.fromCharCode(charcode);
        }
    }
    
    return `${result}`;

}
var z = 'abcd'
console.log(CaesarCipher('vwxyz', [1,2,3,4,5]));



var cars = "vwxyz";
var charCars = cars.split('');
for (var i = 0; i < charCars.length; i++)
{
	charCars[i] = charCars[i].charCodeAt(0)
}

var first = charCars.slice(0,3);
var second = charCars.slice(3,-1);

first = first.map(function(val){return ++val;});

var newArr = first.concat(second);
var result = String.fromCharCode.apply(null, newArr);

console.log(result)
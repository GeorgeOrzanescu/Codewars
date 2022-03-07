
/*
Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000
*/

// elegant solution not mine
function solution(num){
  // convert the number to a roman numeral
  const roman = {
   M: 1000, CM: 900, D: 500, CD: 400, C: 100, XC: 90,
   L: 50, XL: 40, X: 10, IX: 9, V: 5, IV: 4, I: 1,
 };
  let result = '';
  for (var i of Object.keys(roman)) {
    var q = Math.floor(num / roman[i]);
    num -= q * roman[i];
    result += i.repeat(q);
  }
  console.log(result);
  return result;
}

solution(990);
solution(1666);



// THE OVERALL IDEA IS TO ADD THE IN-BETWEEN VALUES
function solution2(number) {
    // convert the number to a roman numeral
    const divider = [1000,900,500,400,100,90,50,40,10,9,5,4,1];
    const symbol = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I'];

    let result = '';
    let temp = number;
    divider.forEach((item,index) => {
      if(temp >= item){
        result += symbol[index].repeat(Math.floor(temp/item));
        temp = temp % item;
      }
    })

    console.log(result);
    return result;
}
solution2(990);
solution(1666);

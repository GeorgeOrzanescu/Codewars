// in this Kata, you will be given a number n (n > 0) and your task will be to return the smallest square number N (N > 0) such that n + N is also a perfect square. If there is no answer, return -1 (nil in Clojure, Nothing in Haskell).

// solve(13) = 36
// //because 36 is the smallest perfect square that can be added to 13 to form a perfect square => 13 + 36 = 49

// solve(3) = 1 // 3 + 1 = 4, a perfect square
// solve(12) = 4 // 12 + 4 = 16, a perfect square
// solve(9) = 16 
// solve(4) = -1



//first attempt but timed out on server > 12000ms

function solve(n){
    for (let i=1;i < n;i++){
        if ((n !== 1 && Math.sqrt(i) % 1 ===0) && (Math.sqrt(n+i) % 1===0)){
            return i
        }
    }
    return -1;
}
  
// second attemt with a while loop
//also timeouts and other errors
// function solve(n) {
//     let i = 1;
//     if (n === 1 || n % 2 === 0){
//         return -1;
//     }
//     while (Math.sqrt(n+i) % 1 !== 0 || Math.sqrt(i) % 1 !== 0 ) {
//         i++;
//     }
//     return i;
// }


//SOLUTION FROM ONLINE
// they are using a smart move they are searching for i smaller than n , because they then return it squared!!

function solve(n){

    let i = 1
  
    while (i < n) {
      if ((Math.sqrt(((i * i) + n)) % 1) === 0) {
        return i * i
      }
      i++
    }
    return -1
  }
  
//MY solution modified after viewing solution online

function solve(n){
    for (let i=1;i < n;i++){
        if ((n !== 1 && Math.sqrt(i*i) % 1 ===0) && (Math.sqrt(n+i*i) % 1===0)){
            return i*i
        }
    }
    return -1;
}

//cleaned up

function solve(n) {
    for (let i = 1;i < n; i++) {
        if (n !== 1 && Math.sqrt((i*i) + n) % 1 === 0){
            return i*i;
        }
    }
    return -1;
}





console.log(solve(7));
console.log(solve(9));
console.log(solve(17));
console.log(solve(88901));
console.log(solve(290101));
console.log(solve(20));
console.log(solve(13));
console.log(solve(2764761561));

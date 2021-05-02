/*
Task
Given a list lst and a number N, create a new list that contains each number of lst at most N times without reordering. For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next [1,2] since this would lead to 1 and 2 being in the getFreq 3 times, and then take 3, which leads to [1,2,3,1,2,3].

*/


// tried getting the number of occurances , but realised this get's messy fast
// function deleteNth(arr,n){
//     const getFreq = {};
//     for (const [idx, el] of arr.entries()) {
//         if (!getFreq[el]) {getFreq[el] = 1}
//         else {getFreq[el] += 1} 
//     }
//     const result= [];
//     for (const i of Object.keys(getFreq)) {
//         console.log(getFreq[i])
//         if (getFreq[i] <= n ){result.push(i)} 
//     }
//     console.log(result)   
//   }


// got an ideea to set the occurance to n and then decrement each time u add the element from given 
// array to returned array

// Not so cool solution but it does the job
function deleteNth(arr,n){
    const getFreq = {};
    for (const [idx, el] of arr.entries()) {
        if (!getFreq[el]) {getFreq[el] = n}
    }
    const result= [];
    
    for (let elem of arr){

        if (!result.includes(elem)){
            result.push(elem);
            getFreq[elem] -= 1;
            }
        
        else{
            if(getFreq[elem] !== 0){getFreq[elem] -= 1; result.push(elem)}
        }
    }
    return result;
  }


  // Simple SOLUTION using filter

  const deleteNth_clean = (arr,n) => {
    let obj={};
    return arr.filter(num => (
      obj[num] = (obj[num] || 0) + 1, //  assign 0 first time else itself + 1
      obj[num] <= n  // condition to pass
    ));
  }


console.log(deleteNth([20,37,20,21], 1) )// [20,37,21]
console.log(deleteNth([1,1,3,3,7,2,2,2,2], 3)) // [1, 1, 3, 3, 7, 2, 2, 2]

console.log(deleteNth_clean([20,37,20,21], 1)) // [20,37,21]
console.log(deleteNth_clean([1,1,3,3,7,2,2,2,2], 3)) // [1, 1, 3, 3, 7, 2, 2, 2]
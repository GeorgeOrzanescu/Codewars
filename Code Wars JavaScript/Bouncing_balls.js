/* A child is playing with a ball on the nth floor of a tall building. The height of this floor, h, is known.

He drops the ball out of the window. The ball bounces (for example), to two-thirds of its height (a bounce of 0.66).

His mother looks out of a window 1.5 meters from the ground.

How many times will the mother see the ball pass in front of her window (including when it's falling and bouncing?

Three conditions must be met for a valid experiment:
Float parameter "h" in meters must be greater than 0
Float parameter "bounce" must be greater than 0 and less than 1
Float parameter "window" must be less than h.
If all three conditions above are fulfilled, return a positive integer, otherwise return -1.

Note:
The ball can only be seen if the height of the rebounding ball is strictly greater than the window parameter.
*/

/*
Example:
- h = 3, bounce = 0.66, window = 1.5, result is 3

- h = 3, bounce = 1, window = 1.5, result is -1 

(Condition 2) not fulfilled).
*/


// test version
function bouncingBall1(h, bounce, window) {
    result = 1;
    tempBounce = h * bounce;
    while (h > 0 && (0 > bounce < 1) && (window < h) && (tempBounce > window)){
        console.log(tempBounce);
        result += 2;
        tempBounce = tempBounce * 0.66;     
    }
    console.log(tempBounce);
    console.log(result);
}


// this version failed on time and 1 case
function bouncingBall2(h, bounce, window) {
    result = 1;
    noParameters = -1;
    tempBounce = h * bounce;
    
    while (h > 0 && (0 > bounce < 1) && (window < h) && (tempBounce > window)){
        
        result += 2;
        tempBounce = tempBounce * bounce;     
    }
    console.log(result);
    return (result >= 1 && tempBounce <= window && bounce < 1) ? result : noParameters;
}



// passes all tests Failed on time !!
function bouncingBall3(h, bounce, window){
    let condition = (h>0 && 0 > bounce < 1 && window < h);
    let tempBounce = h * bounce;
    let result = 1;
    while(condition && tempBounce > window){
        result += 2;
        tempBounce = tempBounce *bounce;
    }
    console.log((condition && result >=1)? result : -1);

}

// this worked--> the problem apparently was with the way it handled 0 > bounce < 1  !!!
function bouncingBall(h, bounce, window){
    let condition = (h>0 && (bounce >0 && bounce < 1) && window < h);
    if(!condition) return -1;
    let tempBounce = h * bounce;
    let result = 1;
    while(tempBounce > window){
        result += 2;
        tempBounce = tempBounce *bounce;
    }
    console.log(result);

}

bouncingBall(3.0, 0.66, 1.5);
bouncingBall(30.0, 0.66, 1.5);
bouncingBall(1.5, 1, 1.5);
bouncingBall(45465455555555555556123433243, 0.99, 4343);

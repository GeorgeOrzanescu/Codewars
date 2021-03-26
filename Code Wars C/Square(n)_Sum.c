
/* Complete the square sum function so that it squares each number passed into it and then sums the results together.

For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.

*/



#include <stddef.h>
#include <stdio.h>



int square_sum(const int *values, size_t count){
    int result = 0;
    for (int num=0; num < count; num++ ){
        result += values[num] * values[num];
    }
    printf("%d",result);
    return result;
};


void main(){
    int nums[] = {2,2,2,5};
    const int *pnums = nums;
    square_sum(pnums,4);
}
/*
Your task is to make two functions, max and min (maximum and minimum) that take a(n) array/vector of integers list as input and outputs, respectively, the largest and lowest number in that array/vector.
*/

#include <stdio.h>

int min(int* array, int arrayLength)
{
    int min = array[0]; //first element
    for (int i=1; i < arrayLength ; i++){
        if(min > array[i]) min = array[i]; // check if next element is smaller , reassign if true
    }
  return min;
}

int max(int* array, int arrayLength)
{
    int max = array[0]; //first element
        for (int i=1; i < arrayLength ; i++){
            if(max < array[i]) max = array[i]; // check if next element is bigger , reassign if true
        }
    return max;
}




void main()
{
    // testing 

    int *nums[] = {42, 54, 65, 87, 0};
    int *nums2[] = {-52, 56, 30, 29, -54, 0, -110};

    int *pnums = nums;
    int *pnums2 = nums2;

    printf("%d\n",min(pnums,5)); // 0
    printf("%d\n",min(pnums2,7));// -110

    printf("%d\n",max(pnums,5)); // 87
    printf("%d\n",max(pnums2,7)); // 56
}

/* 
Simple challenge - eliminate all bugs from the supplied code so that the code runs and outputs the expected value. Output should be the length of the longest word, as a number.

There will only be one 'longest' word. 
*/

#include <stddef.h>
#include <ctype.h>
#include <stdio.h>

size_t find_longest(const char *words) {
  size_t length = 0, max_length = 0;

  const char *pchar = words;

  
  char c;
  while ((c = *pchar++)) {
    
    if (isspace(c)) {
      
      if (length > max_length) {
        max_length = length;
      }
      length = 0;
    } 
    else {
      length++;
    }
  }
  if (length > max_length){  // no bugs just needs this check in case it is the last word in the string
    max_length = length;      
  }
  return max_length;
}

void main(){
    int max = find_longest("George is ninetest mean boy"); //8
    int max1 = find_longest("The quick white fox jumped around the massive dog"); // 7
    int max2 = find_longest("Take me to tinseltown with you"); //10
    int max3 = find_longest("Sausage chops"); // 7
    int max4 = find_longest("Wind your body and wiggle your belly"); //6
    int max5 = find_longest("Lets all go on holiday"); //7

    printf("%d\n",max);
    printf("%d\n",max1);
    printf("%d\n",max2);
    printf("%d\n",max3);
    printf("%d\n",max4);
    printf("%d",max5);
}

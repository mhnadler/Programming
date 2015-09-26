// why all the buzz about fizzbuzz?

#include <stdio.h>

int main(int argc, char **argv)
{
  int     num;
  int     flag;
  char    *output[4] = {"", "fizz", "buzz", "fizzbuzz"};

  for (num = 1; num <= 100; num++)
  {
    // set up flag depending on value of "num"
    flag = ((num % 3) == 0) ? 1 : 0;
    flag |=((num % 5) == 0) ? 2 : 0;
  
    // print text if required, else print the number
    if (flag)
    {
      printf("%s\n", output[flag]);
    }
    else
    {
      printf("%d\n", num);
    }
  }
  return 0;
}

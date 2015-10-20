#include <stdio.h>

struct junk1 {
   int a;
   int b;
   struct {
      int c;
      int d;
   };
};

int main(int argc, char **argv)
{
   struct junk1 k, *p;
   int i,j;

   p = &k;
   i = sizeof(p);
   j = sizeof(*p);

   printf("i = %d, j = %d\n", i, j);
   return 0;
}

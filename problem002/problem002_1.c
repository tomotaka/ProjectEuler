#include <stdio.h>

int main(void) {
  int i, j, tmp, total = 0;
  for (i = 1, j = 1; i < 4000000; ) {
    if (i % 2 == 0) total += i; 
    tmp = i;
    i = i + j;
    j = tmp;
  }
  printf("%d\n", total);
}

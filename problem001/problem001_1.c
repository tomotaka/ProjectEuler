#include <stdio.h>

int main(void) {
  long i, total = 0;
  for (i = 1; i <= 1000; ++i) {
    if (i % 3 == 0 || i % 5 == 0) total += i;
  }
  printf("%ld\n", total);
}


#include <stdio.h>

int main(void) {
  long i, a, b;
  for (i = 1; i <= 100; i++) {
    a += i*i;
    b += i;
  }
  b *= b;
  printf("%ld\n", b-a);
}

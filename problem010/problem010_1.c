#include <stdio.h>
#include <math.h>

#define TRUE 1
#define FALSE 0

#define BOOL int

BOOL is_prime(long n) {
  long i;
  long sqrt_n = (long)sqrt((double)n);
  if (n == 1) return FALSE;
  if (n == 2) return TRUE;
  if (n % 2 == 0) return FALSE;
  for (i = 3; i <= sqrt_n; i+=2) {
    if (n % i == 0) {
      /*printf("%ld is can be devided by %ld\n", n, i);*/
      return FALSE;
    }
  }
  /*printf("%ld is prime\n", n);*/
  return TRUE;
}

int main(void) {
  long i;
  long total = 0;

  printf("sizeof(int)=%ld, sizeof(long)=%ld\n", sizeof(int), sizeof(long));

  for (i = 1; i <= 2000000; ++i) {
    if (is_prime(i)) total += i;
  }
  printf("%ld\n", total);
}

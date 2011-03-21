#include <stdio.h>
#include <math.h>

#define bool int
#define true 1
#define false 0

bool is_prime(long n) {
  long i, sqrt_n;

  if (n == 1) return false;
  if (n == 2) return true;
  if (n % 2 == 0) return false;

  sqrt_n = (long)ceil(sqrt((double)n));

  for (i = 3; i <= sqrt_n; i += 2) {
    if (n % i == 0) return false;
  }

  return true;
}

int main(void) {
  long i, last_found_pn, count = 0;
  for (i = 1; count < 10001; i++) {
    if (is_prime(i)) {
      last_found_pn = i;
      ++count;
    }
  }
  printf("%ld\n", last_found_pn);
}

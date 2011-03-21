#include <stdio.h>
#include <stdlib.h>

#define bool int
#define true 1
#define false 0

long gcd(long a, long b) {
  bool nochange = false;
  long max, i, ret = 1;

  while (!nochange) {
    nochange = true;
    max = a < b ? b : a;
    for (i = 2; i <= max; ++i) {
      if (a % i == 0 && b % i == 0) {
        ret *= i;
        a = a / i;
        b = b / i;
        nochange = false;
        break;
      }
    }
  }
  return ret;
}

long lcm(long a, long b) {
  return (a*b) / gcd(a, b);
}

int main(void) {
  long i, answer = 1;
  for (i = 1; i <= 20; ++i) {
    answer = lcm(answer, i);
  }
  printf("%ld\n", answer);
}

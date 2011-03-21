#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BOOL int
#define TRUE 1
#define FALSE 0

#define N 600851475143

struct factors {
  int size;
  int vecsize;
  long* vector;
};

void add_vec(struct factors* f, long n) {
  int tmpvecsize;
  long *tmpvector;
  if (f->size == f->vecsize) {
    tmpvecsize = f->vecsize;
    tmpvector = (long*)malloc(sizeof(long)*tmpvecsize);
    memcpy(tmpvector, f->vector, sizeof(long)*tmpvecsize);

    free(f->vector);
    f->vecsize = f->vecsize + 10;
    f->vector = (long*)malloc(sizeof(long)*f->vecsize);
    memcpy(f->vector, tmpvector, sizeof(long)*tmpvecsize);
  }
  f->vector[f->size++] = n;
}

struct factors factors(long n) {
  struct factors ret;
  long i;
  BOOL nochange = FALSE;

  ret.size = 0;
  ret.vecsize = 10;
  ret.vector = (long*)malloc(sizeof(long) * ret.vecsize);

  while (!nochange) {
    nochange = TRUE;
    for (i = 2; i < n; i++) { 
      if (n % i == 0) {
        add_vec(&ret, i);
        nochange = FALSE;
        n = n / i;
        break;
      }
    }
  }

  add_vec(&ret, n);
 
  return ret;
}

int main(void) {
  struct factors f;
  long i, max = 0;

  f = factors(N);
  
  for (i = 0; i < f.size; i++) {
    if (max < f.vector[i]) {
      max = f.vector[i];
    }
  }
  printf("%ld\n", max);
}

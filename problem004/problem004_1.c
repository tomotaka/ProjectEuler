#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BOOL int
#define TRUE 1
#define FALSE 0

#define DEFAULT_EXPANSION_SIZE 10

struct nvector {
  int size;
  int vecsize;
  long* vector;
};

struct nvector* nv_create(int size) {
  struct nvector* ret = (struct nvector*)malloc(sizeof(struct nvector));
  ret->size = 0;
  ret->vecsize = size;
  ret->vector = (long*)malloc(sizeof(long)*ret->vecsize);
  return ret;
}

void nv_expand(struct nvector* nv, int expansion_size) {
  int tmp_vs = nv->vecsize;
  long* tmp_v = (long*)malloc(sizeof(long)*tmp_vs);
  memcpy(tmp_v, nv->vector, sizeof(long)*tmp_vs);
  free(nv->vector);
  nv->vecsize += expansion_size;
  nv->vector = (long*)malloc(sizeof(long)*nv->vecsize);
  memcpy(nv->vector, tmp_v, sizeof(long)*tmp_vs);
  free(tmp_v);
}

void nv_add(struct nvector* nv, long value) {
  if (nv->size == nv->vecsize) {
    nv_expand(nv, DEFAULT_EXPANSION_SIZE);
  }
  nv->vector[nv->size++] = value;
}

struct nvector* keta_bunkai(long n) {
  long k;
  long tmp = n;
  struct nvector* nv1 = nv_create(10);
  struct nvector* nv2;
  int i;
  while (10 <= n) {
    k = n % 10;
    n = n / 10;
    nv_add(nv1, k);
  }
  nv_add(nv1, n);

  nv2 = nv_create(nv1->size);
  for (i = nv1->size - 1; 0 <= i; i--) {
    nv_add(nv2, nv1->vector[i]);
  }

  free(nv1);
  return nv2;
}

void nv_free(struct nvector* nv) {
  free(nv->vector);
  free(nv);
}

int is_kaibun(long n) {
  struct nvector* ketas = keta_bunkai(n);
  int size = ketas->size;
  int max = ketas->size / 2;
  int i;
  BOOL result = TRUE;
  for (i = 0; i < max; i++) {
    if (ketas->vector[i] != ketas->vector[size-1-i]) return FALSE;
  }
  nv_free(ketas);
  return result;
}

int main(void) {
  struct nvector* ketas;
  int i, j;
  long tmp, max = 0;

  for (i = 100; i <= 999; ++i) {
    for (j = 100; j <= 999; ++j) {
      tmp = i * j;
      if (max < tmp && is_kaibun(tmp)) {
        max = tmp;
      }
    }
  }
  printf("%ld\n", max);
}



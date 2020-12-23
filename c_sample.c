#include <stdio.h>

int sum (int a, int b){
  return (a + b);
}

int main() {

  int a = 10;
  int b =  20;

  printf("%d, %d, %d", a, b, sum(a, b));

  return 1;
}
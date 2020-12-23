#include <stdio.h>

void increment_score (int *old_score){
  int x = *old_score;
  x += 1;
  printf("Inner Score is: %d", x);
}

void print_add(int* number){
  printf("Number is: %d", *number);
}

int main(void){
  int score = 30;

  print_add(&score);

  return 1;
}
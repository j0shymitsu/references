#include <stdio.h>

int main()
{
  char name[100];           // Fixed length
  printf("Enter name\n");
  scanf("%100s", name);
  printf("Hello %s\n", name);
}
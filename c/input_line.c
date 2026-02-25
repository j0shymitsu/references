#include <stdio.h>

int main()
{
  char line [1000];
  printf("Enter line:\n");
  scanf("%[^\n]1000s", line);     // Regular expression: Read whole line, stop at 1000 chars
  printf("Line: %s\n",line);

  // Safer example
  char line_2 [1000];
  printf("Enter line:\n");
  fgets(line, 1000, stdin);
  printf("Line: %s\n", line);
}
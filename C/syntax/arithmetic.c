#include <stdio.h>    // Include standard input/output library

int main(void)    // Main function declaration, returns no arguments
{
    int a = 6, b = 2, c;    // Declare variables a b and c; initialise a to 6 and b to 2

    c = a + b;    // Assign c as the sum of a and b
    printf("a + b = %d\n", c);    // Print the sum with a descriptive label

    c = a - b;    // Change the value of c to a minus b
    printf("a - b = %d\n", c);    // ""

    c = a * b;    // Change the value of c to the product of a and b
    printf("a x b = %d\n", c);    // ""

    c = a / b;    // Change the value of c to a over b
    printf("a / b = %d", c);    // ""

    return 0;    // Program termination
}
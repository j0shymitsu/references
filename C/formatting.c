#include <stdio.h>

int main(void)
{
    char st[] = "hello, world";
    int y = 58;
    double pi = 3.141593;

    char first_name[] = "Josh";
    char last_name[] = "Birch";

    printf("hello, world\n");
    printf("Printing a string with five leading space: %*s\n", 5, st);
    printf("Hello, my name is: %s %s\n", first_name, last_name);
    printf("Printing an integer: %i\n", y);
    printf("Printing a number with a plus or minus: %+i\n", y);
    printf("Printing a number with two leading spaces and a plus sign: %+*d\n", 5, y);
    printf("Printing the value of Pi to 1 decimal place: %.1f\n", pi);

    return 0;
}
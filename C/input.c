#include <stdio.h>    // Include standard library

int main(void)    // Start the main program; "void" =  takes no args
{
    char st[10];    // Declare an array of characters (string) with a length of 10 (9 characters pluss null terminator)
    int i;    // Declare an integer

    printf("Please enter a string: ");    // Printed statement to prompt for input (doesn't take input)
    scanf("%s", st);    // Input statement, takes the input string, stores it in "st"; doesn't handle spaces

    printf("You entered: %s", st);    // Prints out the inputted string (st)
    printf("\n");    // New line

    printf("Please enter an integer: ");    // Prompt
    scanf("%d", &i);    // Takes an integer (%d), stores it in "i"

    printf("You entered: %d", i);    // Returns an integer (%d), takes it from "i"
    printf("\n");    // New line

    return 0;    // Program exit status
}
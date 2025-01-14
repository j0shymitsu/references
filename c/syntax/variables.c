#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    char character_name[] = "Josh";    // How to store a string as a variable
    int character_age = 30;

    printf("There once was a man named %s.\n", character_name);
    printf("He was %d years old.\n", character_age);

    character_age = 20;    // Variables can change half way through a program

    printf("He really liked the name %s...\n", character_name);
    printf("... but he didn't like being %d.\n", character_age);

    return 0;
}
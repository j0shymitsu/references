#include <stdio.h>
#include <string.h>    // Include the string library

int main(void)
{
    char username[10];

    printf("Please enter your username:\n");
    scanf("%s", &username);

    if(strcmp(username, "Cyber") == 0)    // strcmp = string compare
    {
        printf("--- Welcome Cyber ---");
    }
    else
    {
        printf("Username incorrect.");
    }

    return 0;
}
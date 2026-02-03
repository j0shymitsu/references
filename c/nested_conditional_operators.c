#include <stdio.h>
#include <string.h>

int main(void)
{
    char username[10];
    char password[10];

    printf("\nEnter username: ");
    scanf("%s", username);

    if(strcmp(username, "Josh") == 0)
    {
        printf("\n--- Welcome Josh! ---\n\nPlease enter your password: ");
        scanf("%s", password);

        if(strcmp(password, "joshpass") == 0)
        {
            printf("\n --- Access Granted --- \n");
            return 0;
        }

        else
        {
            printf("\n --- Access Denied ---\n");
            return -2;
        }
    }

    else
    {
        printf("\n --- Incorrect username ---\n");
    }

    return -3;
}
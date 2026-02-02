#include <stdio.h>

int main(void)
{
    int a = 2, b = 2, c = 4;

    printf("a = 2, b = 2, c = 4\n1 = true, 0 = false\n\n");

    printf("a (%d) == b (%d) = %d\n", a, b, a == b);    // == : is equal to
    printf("a (%d) == c (%d) = %d\n", a, c, a == c);   // == : is equal to
    printf("a (%d) > b (%d) = %d\n", a, b, a > b);     // > : is greater than
    printf("a (%d) < c (%d) = %d\n", a, c, a < c);

    return 0;
}
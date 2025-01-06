#include <stdio.h>

int main(void)
{
    int a = 6, c;

    c = 248;    // c becomes equal to 248
    printf("c = %d\n", c);

    c += a;    // The addition of c and a becomes equal to c
    printf("c = %d\n", c);

    c -= a;    // The subtraction of a from c becomes equal to c
    printf("c = %d\n", c);

    c *= a;    // The product of c and a becomes equal to c
    printf("c = %d\n", c);

    c /= a;    // The division of c by a becomes equal to c
    printf("c = %d\n", c);

    return 0;
}
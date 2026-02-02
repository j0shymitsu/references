#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    // integer types
    int i = 42;                     // standard integer
    short s = -123;                 // short integer
    long l = 123456789L;            // long integer
    long long ll = 9876543210LL;    // long long integer; reliable portable 64-bit

    // unsigned types (non-negative)
    unsigned int ui = 300u;
    unsigned long ul = 4000000000UL;

    // char types
    char c = 'A';                       // single character
    unsigned char uc = 200;             // unsigned character; good for raw binary data
    signed char sc = -100;              // signed character
    char character_name[] = "Josh";     // How to store a string as a variable

    // floating-point types
    float f = 3.14f;
    double d = 2.718181828;
    long double ld = 1.6180339887L;

    // printing values
    printf("int: %d\n", i);
    printf("short: %hd\n", s);
    printf("long: %ld\n", l);
    printf("long long: %lld\n", ll);

    printf("unsigned int: %u\n", ui);
    printf("unsigned long: %lu\n", ul);

    printf("char: %c\n", c);
    printf("unsigned char: %u\n", uc);
    printf("signed char: %d\n", sc);

    printf("float: %f\n", f);
    printf("double: %lf\n", d);
    printf("long double: %Lf\n", ld);

    printf("There once was a man named %s.\n", character_name);
    printf("He was %d years old.\n", i);

    i = 20;    // Variables can change half way through a program

    printf("He really liked the name %s...\n", character_name);
    printf("... but he didn't like being %d.\n", i);

    return 0;
}
#include <stdio.h>

int main(void)
{
    float celsius, fahr;
    int lower, upper, step;

    lower = 0;
    upper = 300;
    step = 5;

    printf("Celsius\tFahrenheit\n");

    celsius = lower;
    while(celsius <= upper)
    {
        fahr = (celsius * 9/5) + 32;
        printf("%3.0f\t\t\t%6.1f\n", celsius, fahr);
        celsius = celsius + step;
    }

    return 0;
}
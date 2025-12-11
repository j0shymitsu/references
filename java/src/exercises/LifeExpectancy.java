package exercises;

import java.util.Scanner;

public class LifeExpectancy
{
    public static void main(String[] args)
    {
        Scanner inputScanner = new Scanner(System.in);

        System.out.println("Are you male? (Type 'true' or 'false'):");
        boolean isMale = inputScanner.nextBoolean();

        if(isMale)
        {
            System.out.println("Your life expectancy as a male is around 79 years of age.");
        }
        else
        {
            System.out.printf("Your life expectancy as a female is around 83 years of age.");
        }
    }
}

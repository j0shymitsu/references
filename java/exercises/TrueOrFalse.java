package exercises;

import java.util.Scanner;

public class TrueOrFalse
{
    public static void main(String[] args)
    {
        Scanner inputScanner = new Scanner(System.in);
        System.out.println("Josh:");
        System.out.println("1. I can code in C++");
        System.out.println("2. I can code in Python");
        System.out.println("Which do you think is true? (Enter 1 or 2):");
        int userAnswer = inputScanner.nextInt();

        if(userAnswer == 1)
        {
            System.out.println("Incorrect! The answer was 2!");
        }
        else if (userAnswer == 2)
        {
            System.out.println("Correct! The answer was 2!");
        }
        else
        {
            System.out.println("Invalid input!");
        }
    }
}

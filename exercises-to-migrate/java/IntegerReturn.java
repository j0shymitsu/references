package exercises;

import java.util.Scanner;

public class IntegerReturn
{
    public static void main(String[] args)
    {
        boolean isMorning = true;
        boolean isAfternoon = false;

        char capitalA = 'A';
        char caret = '^';

        int age = 18;
        double goldenRatio = 1.61803398875;

        long possibleLargeNumber = 643125L;
        float speed = 70.3F;

        byte x = 5;
        short y = 2345;


        /* Task */

        Scanner inputScanner = new Scanner(System.in);

        System.out.println("Please type an integer followed by enter: ");
        int someInteger = inputScanner.nextInt();
        inputScanner.nextLine();
        System.out.println("Your integer is " + someInteger);
        System.out.println();

        System.out.println("Please enter a decimal followed by enter: ");
        double someDecimal = inputScanner.nextDouble();
        inputScanner.nextLine();
        System.out.println("Your decimal is " + someDecimal);


    }
}

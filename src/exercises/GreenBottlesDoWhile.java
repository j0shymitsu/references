package exercises;

import java.util.Scanner;

public class GreenBottlesDoWhile 
{
    public static void main(String[] args) 
    {
        Scanner inputScanner = new Scanner(System.in);
        String wallPhrase = " green bottles hanging on the wall";
        int noOfBottles = 10;
        int next = 1;

        do
        {
            System.out.print(noOfBottles + wallPhrase + ",\n");
            System.out.print(noOfBottles + wallPhrase + ",\n");
            System.out.print("And if one green bottle should \"accidentally\" fall, there'd be ");
            noOfBottles -= 1;
            System.out.print(noOfBottles + wallPhrase);
            System.out.println("\n");

            System.out.println("Would you like to another verse? (1 = yes, 2 = no)");
            next = inputScanner.nextInt();
        } while(next == 1);

        System.out.println("Finished!");
    }
}

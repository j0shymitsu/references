package exercises;

import java.util.Scanner;

public class GreenBottlesWhileLoop 
{
    public static void main(String[] args) 
    {
        Scanner scanner = new Scanner(System.in);
        String wallPhrase = " green bottles hanging on the wall";

        System.out.println("How many bottles would you like to start with?");
        int noOfBottles = scanner.nextInt();

        while(noOfBottles > 0)
        {
            if(noOfBottles > 2)
            {
                System.out.print(noOfBottles + wallPhrase + ",\n");
                System.out.print(noOfBottles + wallPhrase + ",\n");
                System.out.print("And if one green bottle should \"accidentally\" fall, there'd be ");
                noOfBottles -= 1;
                System.out.print(noOfBottles + wallPhrase);
                System.out.println("\n");
            }
            else
            {
                wallPhrase = " green bottle hanging on the wall";
                System.out.print(noOfBottles + wallPhrase + ",\n");
                System.out.print(noOfBottles + wallPhrase + ",\n");
                System.out.print("And if one green bottle should \"accidentally\" fall, there'd be ");
                noOfBottles -= 1;
                System.out.print(noOfBottles + " green bottles hanging on the wall.");
                System.out.println("\n");
            }
        }
    }
}

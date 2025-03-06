package exercises;

import java.util.Scanner;

public class ConversionToBinary
{
    public static void main(String[] args)
    {
        Scanner inputScanner = new Scanner(System.in);

        System.out.println("Enter a number to convert to binary: ");
        Integer inputNum = inputScanner.nextInt();
        String binaryNumber = inputNum.toString(inputNum, 2);
        System.out.println();

        System.out.println(inputNum + " in binary:");
        System.out.println(binaryNumber);
    }
}

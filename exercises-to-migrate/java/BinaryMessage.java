package exercises;

import java.util.Scanner;

public class BinaryMessage
{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);

        // prompt for input
        System.out.println("Enter a message: ");
        String message = scanner.nextLine();

        // loop thru each char in string
        for (int i = 0; i < message.length(); i++)
        {
            char character = message.charAt(i);
            String binary = String.format("%08d", Integer.parseInt(Integer.toBinaryString(character)));
            System.out.println(binary);
        }
    }
}

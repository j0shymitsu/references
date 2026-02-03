package portfolio;

import java.util.Scanner;

public class WordleNew
{
    public static void main(String[] args)
    {
        System.out.println("\nWORDLE | NEW GAME\n");
        System.out.println("---------------------------------------------------------------------------------------\n");
        System.out.println("Instructions:\n");
        System.out.println("1. There is a HIDDEN 5 letter word - Try to guess the 5 letter word!\n");
        System.out.println("2. " +
                "If you guess any letters correctly but in the WRONG place, " +
                "they will remain in LOWERCASE.\n");
        System.out.println("3. " +
                "If you guess any letters correctly and they're in the CORRECT place, " +
                "they will remain in UPPERCASE.\n");
        System.out.println("4. " +
                "You have SIX guesses to correct the hidden word, or it's game over! " +
                "After which, the hidden word will be revealed. Let's play!\n\n");
        System.out.println("---------------------------------------------------------------------------------------\n");

        // init
        Scanner scanner = new Scanner(System.in);
        String hiddenWord = "STUDY";
        int numberOfGuesses = 1;

        // game loop
        while (numberOfGuesses <= 6)
        {
            System.out.println("Enter your guess: (guess " + numberOfGuesses + " of 6)\n");

            String userGuess = scanner.nextLine();
            String userGuessFormat = userGuess.trim().toUpperCase();

            if (userGuessFormat.length() != 5)
            {
                System.out.println("Guess must be 5 letters long.");
            }
            else if (userGuessFormat.equals(hiddenWord))
            {
                System.out.println("\nCORRECT! The word was " + hiddenWord + "!");
                System.out.println("You got it correct in " + numberOfGuesses + " guess(es).");
                break;
            }
        }
    }
}


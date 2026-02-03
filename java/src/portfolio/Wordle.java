package portfolio;

import java.util.Scanner;

public class Wordle
{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);

        System.out.println("WORDLE!");
        System.out.println();

        int numOfGuesses = 1;
        String wordToFind = "TAPER";

        while(numOfGuesses <= 6)
        {
            System.out.println("Please enter your 5 letter guess: (guess " + numOfGuesses + " of 6");
            // TODO: format string

            String userGuess = scanner.nextLine();
            String userGuessFormatted = userGuess.trim().toUpperCase();
            int guessLength = userGuessFormatted.length();

            if(guessLength != 5)
            {
                System.out.println("Guess must be 5 letters long!");
            }
            else if(userGuessFormatted.equals(wordToFind))
            {
                System.out.println("\nCorrect! The word was " + wordToFind + "!");
                System.out.println("You got it correct in " + numOfGuesses + " guesses!");
                // TODO: format strings
                break;
            }
            else
            {
                System.out.println("\nIncorrect!");

                for (int i = 0; i < 5; i++)
                {
                    char inWord = Character.toUpperCase(wordToFind.charAt(i));
                    char inGuess = Character.toUpperCase(userGuessFormatted.charAt(i));

                    if(inWord == inGuess)
                    {
                        System.out.println(inWord);
                    }
                    else
                    {
                        continue;
                    }
                }

                System.out.println("| < IN CORRECT PLACE");

                for (int i = 0; i < 5; i++)
                {
                    char inGuess = userGuessFormatted.charAt(i);

                    if(wordToFind.contains(Character.toString(inGuess)) && wordToFind.charAt(i) != inGuess)
                    {
                        System.out.println(inGuess + " ");
                    }
                    else
                    {
                        continue;
                    }
                }
                System.out.println(" | < IN WORD, IN DIFFERENT PLACE\n");
                numOfGuesses += 1;
            }
        }
    }
}

// TODO: Figure out how to store characters for repeat guesses

// TODO: Refactor code completely, really. Bit of a mess

// TODO: Lecturer notes - same letter could appear twice and if guessed twice you wouldn't be able to tell which one was
//  in the right place from the output. // Using techniques learnt so far in the course: you could add the letters to a
//  String. // A more optimal technique which would require further reading: Store the letters in a HashSet. // Be
//  careful to only store wrong characters, as otherwise you can prevent future valid guesses.

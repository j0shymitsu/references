import java.util.Scanner;

public class Wordle {
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);

        System.out.println("WORDLE!");
        System.out.println();

        int noOfGuesses = 1;
        String wordToFind = "TAPER";

        while(noOfGuesses <= 6) 
        {

            System.out.println("Please enter your 5 letter guess: (guess " + noOfGuesses + " of 6)");
            String userGuess = scanner.nextLine();
            String userGuessFormatted = userGuess.trim().toUpperCase();
            int guessLength = userGuessFormatted.length();
            
            if(guessLength != 5)
            {
                System.out.println("Guess must be 5 letters long!\n");
            }

            else if(userGuessFormatted.equals(wordToFind))
            {
                System.out.println("\nCorrect! The word was \"TAPER\".");
                System.out.println("You got it correct in " + noOfGuesses + " guesses!");
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
                        System.out.print(inWord);
                    }
                    else
                    {
                        continue;
                    }
                }
                System.out.println(" | < IN CORRECT PLACE");

                for (int i = 0; i < 5; i++) 
                {
                    char inGuess = userGuessFormatted.charAt(i);

                    if(wordToFind.contains(Character.toString(inGuess)) && wordToFind.charAt(i) != inGuess)
                    {
                        System.out.print(inGuess + " ");
                    }
                    else
                    {
                        continue;
                    }
                }
                System.out.println(" | < IN WORD, IN DIFFERENT PLACE\n");

                noOfGuesses += 1;
                continue;
            }
        }

    }
}

/* Still figuring out best way to store characters for repeat guesses & duplicate letter handling */

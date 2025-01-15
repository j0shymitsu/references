import java.util.Scanner;

public class SpellingBee
{
    /* MAIN */
    public static void main(String[] args) 
    {
        Scanner inputScanner = new Scanner(System.in);

        // declare variables for the middle letter and other letters
        String middleLetter;
        String remainingLetters;
        String guessWord;

        // ask user to enter the middle letter
        System.out.println("Enter the middle letter: ");
        middleLetter = inputScanner.nextLine();

        // ask user to enter the other letters
        System.out.println("Enter other letters:");
        remainingLetters = inputScanner.nextLine();

        // concatenate middle letter and other letters into a single set
        String letterPool = middleLetter + remainingLetters;

        // start loop to accept word until user exits
        while(true)
        {
            // check if user exits
            System.out.println("Enter a word with at least 4 letters, or type 'X' to exit:");
            guessWord = inputScanner.nextLine();

            if(guessWord.equals("X"))
            {
                break;
            }
            // validate word w method
            if(validWord(guessWord, middleLetter, letterPool))
            {
                System.out.println("valid");
            }
            else
            {
                System.out.println("invalid");
            }
        }
    }
    
    /* METHOD TO CHECK IF WORD IS VALID */
    public static boolean validWord(String word, String middleLetter, String letterPool)
    {
        // check if word has at least 4 letters
        if(word.length() < 4)
        {
            return false;
        }
        // check if word contains middle letter
        if(!word.contains(middleLetter))
        {
            return false;
        }
        // check if word only uses allowed letters
        for(char n : word.toCharArray())
        {
            if(!letterPool.contains(String.valueOf(n)))
            {
                return false;
            }
        }
        // if all checks = true, valid word
        return true;
    }
}

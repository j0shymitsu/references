package portfolio;

import java.util.ArrayList;
import java.util.Scanner;

public class TaskOne {

    public static void main(String[] args) {
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
                "You have FIVE guesses to correct the hidden word, or it's game over! " +
                "After which, the hidden word will be revealed. Let's play!\n\n");
        System.out.println("---------------------------------------------------------------------------------------\n");

        // init
        Scanner scanner = new Scanner(System.in);
        String hiddenWord = "STUDY";
        int numberOfGuesses = 0;

        // game loop
        while (numberOfGuesses < 5) {
            return;
        }
    }

    public String wordChecker(String hiddenWord, String guessWord) {
        return null;
    }


}


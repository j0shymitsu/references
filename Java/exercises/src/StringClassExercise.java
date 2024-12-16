import java.util.Scanner;

public class StringClassExercise 
{
    public static void main(String[] args) 
    {
        String coldplaySong = "The hardest part";
        String phrase = "Hello world";
        String catPhrase = "    The cat sat on the mat   ";
        String progLanguage = "Java";
        String word = "encodes";

        int phraseLength = phrase.length();
        char seventhLetter = phrase.charAt(6);
        String amendedSongTitle = coldplaySong.replace('p', 'f');
        String trimmedPhrase = catPhrase.trim();
        int indexOfA = progLanguage.indexOf('a');
        int indexOfV = progLanguage.indexOf('v');
        int indexOfZ = progLanguage.indexOf('z');
        String partOfWord = word.substring(2, 6);
        /* Other methods include:
         * equalsIgnoreCase()
         * startsWith()
         * endsWith()
         * toLowerCase()
         * toUpperCase()
         * contains()
         */

        System.out.println(amendedSongTitle);  
        System.out.println(phraseLength);
        System.out.println(seventhLetter);
        System.out.println(trimmedPhrase);
        System.out.print(indexOfA + "\n");
        System.out.print(indexOfV + "\n");
        System.out.print(indexOfZ + "\n");
        System.out.println(partOfWord);
        System.out.println();


        /* TASKS */
        // Get string, remove trailing and leading whitespace, output how many chars the remaining phrase has
        Scanner scanner = new Scanner(System.in);

        System.out.println("Please enter a sentence:");
        String sentence = scanner.nextLine();
        String noWhitespace = sentence.trim();
        int sentenceLength = noWhitespace.length();
        System.out.println(sentenceLength);
        System.out.println();

        // Get string, if it has more than 10 char, print the last 5, otherwise, print all
        if(sentenceLength > 10)
        {
            String partOfSentence = sentence.substring(sentence.length() - 5);
            System.out.println(partOfSentence);
        }
        else
        {
            System.out.println(noWhitespace);
        }

        // If it has more than 30 characters, take the first 27, add an elipsis and print that. Else, print whole
        // string
    /*  Scanner scanner = new Scanner(System.in);

        System.out.println("Please enter a sentence: ");
        String sentence = scanner.nextLine();

        int sentenceLength = sentence.length();

        if(sentenceLength > 30)
        {
            sentence = sentence.substring(0, 27);
            sentence = sentence + "...";
            System.out.println(sentence);
        }
        else
        {
            System.out.println(sentence);
        }
    */
        
        // If the phrase ends in the word "like", remove this from the phrase and print
    /* 
        Scanner scanner = new Scanner(System.in);

        System.out.println("Please enter a sentence: ");
        String sentence = scanner.nextLine();

        boolean hasLike = sentence.endsWith("like");

        if(hasLike)
        {
            sentence = sentence.substring(0, sentence.lastIndexOf("like")).trim();
            System.out.println(sentence);
        }
        else
        {
            System.out.println(sentence);
        }
    */   
    
        // Check for words: Java, code, or String (non-case sensitive), and if it contains any, print. Otherwise ask for a 
        // new string

    }    
}

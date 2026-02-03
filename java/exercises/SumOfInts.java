package exercises;

import java.util.ArrayList;

public class SumOfInts
{
    public static void main(String[] args)
    {
        // consider the following sentence: "she had 4 cats, 3 hamsters, 2 dogs, and 12 pet fish
        // programmatically determine how many animals there are in total
        String sentence = "she had 4 cats, 3 hamsters, 2 dogs, and 12 pet fish";
        int total = totalOfIntsInSentence(sentence);
        System.out.println("There are " + total + " animals");
    }

    static int totalOfIntsInSentence(String sentence)
    {
        // break sentence into words
        ArrayList<String> words = wordsFromSentence(sentence);
        int total = 0;

        for (String word : words)
        {
            // check each word for a value
            try
            {
                int wordValue = Integer.parseInt(word);
                total += wordValue;
            }
            catch(Exception e)
            {
                // no need to do anything
            }
            // sum
        }
        return total;
    }

    static ArrayList<String> wordsFromSentence(String sentence)
    {
        ArrayList<String> words = new ArrayList<String>();
        String currentWord = "";

        for (int i = 0; i < sentence.length(); i++)
        {
            if(sentence.charAt(i) == ' ')
            {
                words.add(currentWord);
                currentWord = "";
            }
            else
            {
                currentWord += sentence.charAt(i);
                if(i == sentence.length() - 1)
                {
                    words.add(currentWord);
                }
            }
        }

        return words;
    }
}

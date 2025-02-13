package exercises;

import java.util.Scanner;

public class Sentence
{
    public static void main(String[] args) 
    {
        Scanner scanner = new Scanner(System.in);

        String sentence = "";
        String sentenceLowercase = "";
            
        boolean hasJava = sentenceLowercase.contains("java");
        boolean hasCode = sentenceLowercase.contains("code");
        boolean hasString = sentenceLowercase.contains("string");
        
        while (!hasJava && !hasCode && !hasString)
        {
            System.out.println("Please enter a new sentence: ");
            sentence = scanner.nextLine();
            sentenceLowercase = sentence.toLowerCase();
        } 

        System.out.println(sentence);
    }    
}

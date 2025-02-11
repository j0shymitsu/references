package syntax;

import java.util.Scanner;

public class MethodMultipleParameters 
{
    public static void main(String[] args) 
    {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Type a phrase");
        String phrase = scanner.nextLine();

        trimWithElipsis(phrase, 5);
    }
    
    static void trimWithElipsis(String text, int length)
    {
        if(text.length() > length)
        {
            String shortPhrase = text.substring(0, length).trim() + "...";
            System.out.println(shortPhrase);
        }
        else
        {
            System.out.println(text);
        }   
    }  
}

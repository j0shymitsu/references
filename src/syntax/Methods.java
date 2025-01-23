import java.util.Scanner;

/* Methods are normally tied to a class; Functions are independent */
public class Methods 
{
    public static void main(String[] args) 
    {
        printMenu(3);
        Scanner scanner = new Scanner(System.in);
        System.out.println("hello all");

        char someLetter = "hello".charAt(3);
    }    

    static void printMenu(int numberOfTimes)
    {
        for (int i = 0; i < numberOfTimes; i++) 
        {
            System.out.println("****MENU****");    
        }
        
    }

    static int multiply(int a, int b, int c)
    {
        int result = a * b * c;
        return result;
    }

    static int numberToOwnPower(int number)
    {
        int total = number;
        for(int i=1; i < number; i++)
        {
            total *= number;
        }

        return total;
    }
}

import java.util.Calendar;
import java.util.GregorianCalendar;
import java.util.Scanner;

public class AgeCalc
{
    static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) 
    {
        System.out.println("Age calculator");
        while(true)
        {
            printMenu();
            int choice = getUserInteger("Type a number to make a choice");
            if(choice == 1)
            {
                calculateAge();
            }
            if(choice == 2)
            {
                calculateFutureAge();
            }
            if(choice == 3)
            {
                break;
            }
        }
    }

    static void printMenu()
    {
        System.out.println("Menu");
        System.out.println("1. Calculate my age now");
        System.out.println("2. Calculate my age in future");
        System.out.println("3. Exit");    
    }

    static int getCurrentYear()
    {
        Calendar gregorianCalendar = new GregorianCalendar();
        return gregorianCalendar.get(Calendar.YEAR);
    }

    static int getUserInteger(String message)
    {
        System.out.println(message);
        return scanner.nextInt();
    }

    static void calculateAge()
    {
        int yearOfBirth = getUserInteger("Please type your year of birth");

        int currentYear = getCurrentYear();
        int age = currentYear - yearOfBirth;
        System.out.println("You are about " + age + " years old.");
            
    }

    static void calculateFutureAge()
    {
            
        int age = getUserInteger("Please type your age");

        int futureYear = getUserInteger("Please type the year you wish to know your age in");

        int currentYear = getCurrentYear();
        int futureAge = futureYear - currentYear + age;
        System.out.println("You will be " + futureAge + " in " + futureYear);
            
    }
}

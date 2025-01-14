import java.util.Scanner;

public class DrivingLicense
{
    public static void main(String[] args) 
    {
        Scanner inputScanner = new Scanner(System.in);

        System.out.println("How old are you?");
        int age = inputScanner.nextInt();
        inputScanner.nextLine();

        System.out.println("Do you have a valid license with provisional motorcycle entitlement? (Type true or false)");
        boolean hasLicense = inputScanner.nextBoolean();
        inputScanner.nextLine();

        System.out.println("Do you have a valid CBT certificate? (Type true or false)");
        boolean hasCBT = inputScanner.nextBoolean();
        inputScanner.nextLine();

        System.out.println("Do you have a valid theory test certificate? (Type true or false)");
        boolean hasTheory = inputScanner.nextBoolean();
        inputScanner.nextLine();

        if(age >= 17 && hasLicense && hasCBT && hasTheory)
        {
            System.out.println("You can drive an A1 light motorcycle.");
        }
        else
        {
            System.out.println("You may not drive a motorcycle.");
        }
    }    
}

import java.util.ArrayList;
import java.util.Scanner;

public class ZooNames
{
    public static void main(String[] args)
    {
        // initialise ArrayList for animals
        ArrayList<String> animalList = new ArrayList<String>();

        // initialise scanner
        Scanner inputScanner = new Scanner(System.in);

        // while loop to prompt for names; check for already existing
        while(true)
        {
            System.out.println("Enter new animal into database (or 'X' to exit): ");
            String newAnimal = inputScanner.nextLine();
            String exitCharacter = "x";

            if(newAnimal == exitCharacter)
            {
                break;
            }

        }
    }
}

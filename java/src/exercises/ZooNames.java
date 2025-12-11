package exercises;
import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;
import java.util.ArrayList;
import java.util.Scanner;

public class ZooNames
{
    // initialise scanner
    static Scanner inputScanner = new Scanner(System.in);

    public static void main(String[] args)
    {
        // initialise ArrayList for animals
        ArrayList<String> animalNames = new ArrayList<String>();

        // while loop to prompt for names
        while(true)
        {
            System.out.println("\nWould you like to enter a new animal into the database? [Type 'yes' and hit enter; else type anything else and hit enter.]");

            String cont = inputScanner.nextLine();
            cont = cont.toUpperCase();

            if (cont.equals("YES"))
            {
                System.out.println("\nEnter animal name: ");
                String animalName = inputScanner.nextLine();
                // loop calling methods here
                isNameUnique(animalNames, animalName);
            }
            else
            {
                break;
            }
        }

        System.out.println("\nAnimals now in database: ");
        for (String animalName : animalNames)
        {
            System.out.println(animalName);
        }

        arrayListToFile(animalNames);
    }

    // method to handle user input
    static void isNameUnique(ArrayList<String> animalNames, String animalName)
    {
        animalName = animalName.toUpperCase();
        if(animalNames.contains(animalName))
        {
            System.out.println("\nAnimal name already in database! Please try another.");
        }
        else
        {
            animalNames.add(animalName);
            System.out.println("\nAnimal " + animalName + " added to database!");

        }
    }

    // method to write to file
    private static void arrayListToFile(ArrayList<String> arrayList)
    {
        Path location = Paths.get("data/zoonames.txt");
        Charset utf8 = StandardCharsets.UTF_8;

        try
        {
            Files.write(location, arrayList, utf8, StandardOpenOption.APPEND);
        }
        catch (IOException e)
        {
            System.out.println("The file could not be saved");
        }
    }
}

package exercises;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class MixedList
{
    public static void main(String[] args)
    {
        ArrayList<String> strings = new ArrayList<>();
        ArrayList<Integer> integers = new ArrayList<>();
        File dataFile = new File("data/stringint.txt");

        try
        {
            Scanner fileScanner = new Scanner(dataFile);

            while(fileScanner.hasNext())
            {
                if(fileScanner.hasNextInt())
                {
                    integers.add(fileScanner.nextInt());
                    fileScanner.nextLine();
                }
                else
                {
                    strings.add(fileScanner.nextLine());
                }
                fileScanner.close();
            }
        }
        catch(FileNotFoundException e)
        {
            System.out.println("Cannot read from file");
        }

        System.out.println("Strings: ");
        for (String string : strings)
        {
            System.out.println(string);
        }

        System.out.println(System.lineSeparator() + "Integers: ");
        for (Integer integer : integers)
        {
            System.out.println(integer);
        }
    }
}

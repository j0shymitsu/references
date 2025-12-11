package exercises;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class NameList
{
    public static void main(String[] args)
    {
        ArrayList<String> namesList = arrayListFromDataFile();
        for (String name : namesList)
        {
            System.out.println(name);
        }
    }

    static ArrayList<String> arrayListFromDataFile()
    {
        ArrayList<String> nameList = new ArrayList<String>();
        File dataFile = new File("data/names.txt");

        try
        {
            Scanner fileScanner = new Scanner(dataFile);

            while(fileScanner.hasNext())
            {
                nameList.add(fileScanner.nextLine());
            }

            fileScanner.close();
        }
        catch(FileNotFoundException e)
        {
            System.out.println("Cannot read from file");
        }

        return nameList;
    }
}

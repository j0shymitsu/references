package exercises;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class NumList
{
    public static void main(String[] args)
    {
        ArrayList<Integer> numList = arrayListFromDataFile();
        int sum = 0;
        int total = numList.size();

        for (Integer i : numList)
        {
            System.out.print(i + ", ");
            sum += i;
        }

        System.out.println();

        int avg = sum / total;

        System.out.println("Average: " + avg);

    }

    static ArrayList<Integer> arrayListFromDataFile()
    {
        ArrayList<Integer> numList = new ArrayList<>();
        File dataFile = new File("data/nums.dat");

        try
        {
            Scanner fileScanner = new Scanner(dataFile);

            while(fileScanner.hasNext())
            {
                numList.add(fileScanner.nextInt());
            }

            fileScanner.close();
        }
        catch(FileNotFoundException e)
        {
            System.out.println("Cannot read from file");
        }

        return numList;
    }
}

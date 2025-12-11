package exercises;

import java.util.Scanner;

public class ModuleResults
{
    public static void main(String[] args)
    {
        Scanner inputScanner = new Scanner(System.in);

        int[] predictedResults = new int[6];
        float avgResult = 0;

        for (int i = 0; i < predictedResults.length; i++)
        {
            System.out.println("Enter your predicted result for module " + (i + 1) + ":");
            predictedResults[i] = inputScanner.nextInt();
        }

        for (int predictedResult : predictedResults)
        {
            avgResult += predictedResult;
        }

        avgResult = (avgResult / 6);

        if(avgResult < 40)
        {
            System.out.println("Your average is " + avgResult + "%. This is classed as a fail.");
        }
        else if(avgResult < 50)
        {
            System.out.println("Your average is " + avgResult + "%. This is classed as a 3rd.");
        }
        else if(avgResult < 60)
        {
            System.out.println("Your average is " + avgResult + "%. This is classed as a 2:2.");
        }
        else if(avgResult < 70)
        {
            System.out.println("Your average is " + avgResult + "%. This is classed as a 2:1.");
        }
        else
        {
            System.out.println("Your average is " + avgResult + "%. This is classed as a 1:1.");
        }



    }
}

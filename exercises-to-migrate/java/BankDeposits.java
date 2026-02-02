package exercises;

public class BankDeposits
{
    public static void main(String[] args)
    {
        int[] bankDeposits = {2999, 7000, 2000, 35000};
        int runningTotal = 0;

        for (int i = 0; i < bankDeposits.length; i++)
        {
            int individualDeposit = bankDeposits[i];
            runningTotal += individualDeposit;
        }

        System.out.println("Total deposits: " + runningTotal);
    }
}

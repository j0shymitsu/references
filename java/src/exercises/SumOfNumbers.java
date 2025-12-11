package exercises;

public class SumOfNumbers
{
    // main method where methods are called
    public static void main(String[] args)
    {
        int testNumber = 4;    // number to pass into method (as per example)

        System.out.println(sumOfNumbersFromOneToN(testNumber));   // print to console the method with test number as
        // value

    }

    // method you want written, returns an int and takes int "n" as argument (brackets)
    static int sumOfNumbersFromOneToN(int n)
    {
        int total = 0;     // initialise running total to be returned at end

        for (int i = 0; i <= n; i++)    // counter that counts from 0 to number "n"
        {
            total += i;    // add "i" to total until "i" reaches the same value as "n"
        }

        return total;    // send the total back
    }
}

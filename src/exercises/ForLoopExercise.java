package exercises;

/*
TASK 1

For each of the following sequences, create a command line programme, and use the For loop syntax generator to get the code for a loop, add the relevent code as neccesary inside the loop, check that the result is as expected:

Starting at 23 going up 4 at a time, print numbers upto and including 123.
Starting at 44 going up 4 at a time, print numbers upto and including 65 (if applicable)
Starting at -20, going up 10 at a time, print the numbers up to, but not including 100. Name the counter "x"
Starting at -55, going down 1 at a time, print the numbers down to and including -77. Name the counter "i"
Starting at 5, going up 5 at a time, print the numbers up to and including 3
*/

public class ForLoopExercise
{
    public static void main(String[] args)
    {
        for (int i = 23; i <= 123; i += 4)
        {
            System.out.println(i);
        }
        System.out.println();

        //

        for (int i = 44; i <= 65; i += 4)
        {
            System.out.println(i);
        }
        System.out.println();

        //

        for (int x = -20; x < 100; x += 10)
        {
            System.out.println(x);
        }
        System.out.println();

        //

        for (int i = -55; i >= -77; i--)
        {
            System.out.println(i);
        }
        System.out.println();

        //

        for (int i = 5; i <= 3; i += 5)
        {
            System.out.println(i);
        }


    }
}

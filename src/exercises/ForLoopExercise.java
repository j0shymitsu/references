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
/*
TASK 2

Complete the following tasks in the same format, but this time write the code yourself, using an example on the page above as reference if needed. Check each loop behaves as expected and then delete all the loop code before starting the next task

Starting at 3, going up 1 at a time, print the numbers up to and including 7
Starting at -5, going up 1 at a time, print the numbers up to but not including 7. Name the counter
Starting at -36, going up 9 at a time, print the numbers up to, but not including 56 (if applicable). Name the counter
Starting at -5, going down 1 at at a time, print the numbers down to and including -17
Starting at 11, going up 2 at a time, print the numbers up to and including 8
*/

        for (int i = 3; i <= 7; i++)
        {
            System.out.println(i);
        }
        System.out.println();

        //

        for (int counter = -5; counter < 7; counter++)
        {
            System.out.println(counter);
        }
        System.out.println();

        //

        for (int i = -36; i < 56; i += 9)
        {
            System.out.println(i);
        }
        System.out.println();

        //

        for (int i = -5; i >= -17; i--)
        {
            System.out.println(i);
        }
        System.out.println();

        //

        for (int i = 11; i <= 8; i += 2)
        {
            System.out.println(i);
        }
        System.out.println();

        //

 /*
TASK 3
Use a for loop to calculate the factorial of 10 (this is 10 x 9 x 8 x 7 etc. all the way to 1). For reference, the answer is 3,628,800
Use a for loop to print out the various hours in the day in the following format:
0:00am
1:00am
2:00am
3:00am
...
11:00am
12:00pm
1:00pm
...
11:00pm
*/
        int total = 1;
        for (int i = 10; i >= 1; i--)
        {
            total = total * i;
        }
        System.out.println(total);
        System.out.println();
        
        //

        for (int hr = 0; hr < 24; hr++)
        {
            int displayHour = (hr == 0 || hr == 12) ? 12 : hr % 12;
            String period = (hr < 12) ? "am" : "pm";
            System.out.println(displayHour + ":00" + period);
        }
        System.out.println();

        //

/*
Advanced task
Using two loops (one inside the other), print out all the minutes of a day using the 24 hour clock. The start of the output would be as follows:

0:00
0:01
0:02
...
*/

        for (int hr = 0; hr < 24; hr++)
        {
            for (int min = 0; min < 60; min++)
            {
                System.out.printf("%d:%02d%n", hr, min);
            }
        }
    }
}

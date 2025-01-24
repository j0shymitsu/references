public class HoursAndMinutes
{
    public static void main(String[] args) 
    {
        /* 1.1 */
        for(int i = 23; i <= 123; i += 4)
        {
            System.out.println(i);
        }
        System.out.println();

        /* 1.2 */
        for(int i = 44; i <= 65; i += 4)
        {
            System.out.println(i);
        }
        System.out.println();

        /* 1.3 */
        for(int x = -20; x < 100; x += 10)
        {
            System.out.println(x);
        }
        System.out.println();

        /* 1.4 */
        for(int i = -55; i >= -77; i--)
        {
            System.out.println(i);
        }
        System.out.println();



        /* 2.1 */
        for(int count = 3; count <= 7; count++)
        {
            System.out.println(count);
        }
        System.out.println();

        /* 2.2 */
        for(int counter = -5; counter < 7; counter++)
        {
            System.out.println(counter);
        }
        System.out.println();

        /* 2.3 */
        for(int i = -36; i < 56; i += 9)
        {
            System.out.println(i);
        }
        System.out.println();

        /* 2.4 */
        for(int i = -5; i >= -17; i--)
        {
            System.out.println(i);
        }
        System.out.println();



        /* 3.1 */
        int factorial = 1;

        for(int i = 10; i > 0; i--)
        {
            factorial *= i;
        }

        System.out.println(factorial);
        System.out.println();

        /* 3.2 */
        for(int i = 0; i <= 24; i++)
        {
            String suffix = ":00";
            
            if(i < 12)
            {
                suffix += "am";
            }
            else
            {
                suffix += "pm";
            }

            int hr = i;
            if(i > 12)
            {
                hr -= 12;
            }
            System.out.println(hr + suffix);
        }
        System.out.println();

        /* 3.3 */
        for(int hr = 0; hr < 24; hr++)
        {
            for(int min = 0; min < 60; min++)
            {
                System.out.printf("%d:%02d%n", hr, min);
            }
        }
    }   
}

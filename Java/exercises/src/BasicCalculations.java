public class BasicCalculations 
{
    public static void main(String[] args) 
    {
        int a = 4 + 3;    // a is 7
        int b = a + 7;    // b is 14
        int c = a + b;    // c is 21
        
        int result = 9 / 4;    // result is 2, not 2.5

        // The remainder
        int sweetsInPacket = 23;
        int noOfChildren = 3;
        int sweetsPerChild = sweetsInPacket / noOfChildren;    // result is 7
        int sweetsLeftForDad = sweetsInPacket % noOfChildren;    // result is 2

        /* CAVEATS WITH NUMBERS */
        // Integer types
        int x = 2147483647;
        x = x + 1;
        System.out.println(x);

        // Currency
        double money = 4.4;
        double money2 = 6.6;
        double result2 = money2 / money;

        // Values that do not change
        final double pi = 3.14159265359;
    }    
}

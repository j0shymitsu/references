public class Fibonacci 
{
    public static void main(String[] args) 
    {
        int fib = 0;
        int next = 1;
        
        while(fib <= 144)
        {
            System.out.println(fib);
            System.out.println(next);
            fib = fib + next;
            next = fib + next;
        }

    }       
}

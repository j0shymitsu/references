package exercises;

public class Facade
{
    public static void main(String[] args)
    {
        String text = "FACADE";
        int number = Integer.valueOf(text, 16);

        if(number > 6)
        {
            System.out.println("x");
        }
        else if( number < 0)
        {
            System.out.println("y");
        }
        else
        {
            System.out.println("z");
        }
    }
}

package exercises;

public class LessThanMoreThan
{
    public static void main(String[] args) 
    {
        for (int i = 0, j = 200; i <= 100 && j >= 0; i++, j -= 2) 
        {
            System.out.println(i + ":" + j);    
        }
        System.out.println();
        
        for (long i = 1, j = 1; i <= 60; i++, j = j * 2) 
        {
            System.out.println(i + ":" + j);
        }
    }
}

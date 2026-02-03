package exercises;

public class OperatorPrecedence
{
    public static void main(String[] args)
    {
        int a = 1 + 2 - 3 / 4 * 5;
        int b = 1 - 2 / 3 * 4 - 5;
        int c = 1 / 2 * 3 + 4 - 5;
        int d = 1 * 2 + 3 - 4 / 5;
        int e = 1 * (2 + 3) - 4 / 5;
        int f = (1 * (2 + 3) - 4) / 5;
        int g = 3 / 2 - 2;
        // int h = 3 / (2 - 2);

        System.out.println(a);
        System.out.println(b);
        System.out.println(c);
        System.out.println(d);
        System.out.println(e);
        System.out.println(f);
        System.out.println(g);
        // System.out.println(h);
    }
}

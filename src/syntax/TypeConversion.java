package syntax;

public class TypeConversion
{
    public static void main(String[] args)
    {
        int number = 42;
        String numberAsString = "42";
        String result = "Result " + number;    // implicit conversion

        String numberAsText = String.valueOf(number);    // explicit conversions
        String numberAsText2 = Integer.toString(number);
        String numberWithSpecifiedBase = Integer.toString(42, 16);    // radix = base of number system

        System.out.println(numberAsText);
        System.out.println(numberAsText2);
        System.out.println(numberWithSpecifiedBase);
    }
}

package exercises;

import java.text.DecimalFormat;

public class DecimalFormatter
{
    public static void main(String[] args)
    {
        DecimalFormat formatter = new DecimalFormat("#.0");
        DecimalFormat fourDigit = new DecimalFormat("00.00##");

        double assignmentWeighting = 0.63;
        int assignmentGrade = 65;
        double examWeighting = 0.37;
        int examGrade = 55;
        double assignmentValue = assignmentWeighting * assignmentGrade;
        double examValue = examWeighting * examGrade;
        double moduleTotal = assignmentValue + examValue;
        String moduleTotalString = formatter.format(moduleTotal);

        double rawValueOne = 0.12345;
        double rawValueTwo = 123.100003;
        double rawValueThree = 40.700200;
        double rawValueFour = 321.12999;
        String rawOneString = fourDigit.format(rawValueOne);
        String rawTwoString = fourDigit.format(rawValueTwo);
        String rawThreeString = fourDigit.format(rawValueThree);
        String rawFourString = fourDigit.format(rawValueFour);

        System.out.println("Your module grade is " + moduleTotalString);

        System.out.println(rawOneString);
        System.out.println(rawTwoString);
        System.out.println(rawThreeString);
        System.out.println(rawFourString);
    }
}

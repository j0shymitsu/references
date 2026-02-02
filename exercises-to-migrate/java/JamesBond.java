package exercises;

public class JamesBond implements Comparable<JamesBond>
{
    private String name;
    private int yearOfBirth;

    String getName()
    {
        return name;
    }

    public int getYearOfBirth()
    {
        return yearOfBirth;
    }


    private int greatness;    // how good a bond they were

    // bondNumber indicates the order in which they starred in their first James Bond film
    JamesBond(int bondNumber)
    {
        switch (bondNumber)
        {
            case 1:
                name = "Connery";
                greatness = 5;
                yearOfBirth = 1930;
                break;
            case 2:
                name = "Lazenby";
                greatness = 1;
                yearOfBirth = 1939;
                break;
            case 3:
                name = "Moore";
                greatness = 4;
                yearOfBirth = 1927;
                break;
            case 4:
                name = "Dalton";
                greatness = 3;
                yearOfBirth = 1946;
                break;
            case 5:
                name = "Brosnan";
                greatness = 3;
                yearOfBirth = 1953;
                break;
            case 6:
                name = "Craig";
                greatness = 6;
                yearOfBirth = 1968;
                break;
            default:
                name = "Imposter";
                greatness = 0;
        }
    }

    @Override
    public int compareTo(JamesBond otherBond)
    {
        return this.greatness - otherBond.greatness;
    }
}

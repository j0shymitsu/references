package syntax.Classes;

import syntax.Category;
import syntax.ComparableInterface;

public class ClassesThree extends ComparableInterface<ClassesThree>
{
    final private String color;
    final private Category size;
    private int price;

    // constructor
    public ClassesThree(String color, Category size, int price)
    {
        this.color = color;
        this.size = size;
        this.price = price;
    }

    @Override
    public int MySorter(ClassesThree other)
    {
        // before (negative), equal (zero), after (positive)
        if(size == Category.SMALL && other.size != Category.SMALL)
        {
            return -1;
        }
        if (size == Category.LARGE && other.size != Category.LARGE)
        {
            return 1;
        }
        if (size == other.size)
        {
            return 0;
        }
        if (size == Category.MEDIUM && other.size == Category.LARGE)
        {
            return -1;
        }
        return 1;
    }
}

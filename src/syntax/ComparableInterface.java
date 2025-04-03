package syntax;

import syntax.Classes.ClassesThree;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public abstract class ComparableInterface<C>
{
    public static void main(String[] args)
    {
        List<String> names = new ArrayList<>();
        names.add("Janet");
        names.add("Heidi");
        names.add("Eleanor");
        names.add("Tom");
        names.add("Jason");

        Collections.sort(names);

        System.out.println(names);

        //
        ArrayList<ClassesThree> tShirts = new ArrayList<>();
        tShirts.add(new ClassesThree("brown", Category.MEDIUM, 999));
        tShirts.add(new ClassesThree("red", Category.LARGE, 499));
        tShirts.add(new ClassesThree("green", Category.SMALL, 1299));

        Collections.sort(tShirts);
    }

    public abstract int MySorter(ClassesThree other);
}


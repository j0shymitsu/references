package exercises;

import java.util.ArrayList;

public class ArrayListsPuzzle
{
    public static void main(String[] args)
    {
        ArrayList<Integer> intList = new ArrayList<>();
        intList.add(1);
        intList.add(2);
        intList.add(3);
        int two = 2;
        intList.remove(two);

        ArrayList<Integer> intList2 = new ArrayList<>();
        intList2.add(1);
        intList2.add(2);
        intList2.add(3);
        Integer two2 = 2;
        intList2.remove(two2);

        System.out.println(intList);    // removes the index 2; because primitive value
        System.out.println(intList2);   // removes the number 2; because object
    }
}

package exercises;

import java.util.ArrayList;
import java.util.Iterator;

public class RemoveFromCollection
{
    public static void main(String[] args)
    {
        ArrayList<String> namesList = new ArrayList<>();

        Iterator<String> namesIterator = namesList.iterator();

        while(namesIterator.hasNext())
        {
            String name = namesIterator.next();
            System.out.println(name);
        }
    }
}

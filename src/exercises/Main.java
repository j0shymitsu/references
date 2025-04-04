package exercises;

import syntax.Sorting.JamesBondAgeComparator;

import java.util.ArrayList;
import java.util.Collections;

public class Main
{
    public static void main(String[] args)
    {
        // james bond
        JamesBond georgeLazenby = new JamesBond(2);
        JamesBond danielCraig = new JamesBond(6);
        JamesBond pierceBrosnan = new JamesBond(5);

        ArrayList<JamesBond> bonds = new ArrayList<>();
        bonds.add(georgeLazenby);
        bonds.add(danielCraig);
        bonds.add(pierceBrosnan);

        Collections.sort(bonds);

        for (JamesBond bond : bonds)
        {
            System.out.println(bond.getName());
        }

        System.out.println();

        //

        JamesBondAgeComparator comparator = new JamesBondAgeComparator();
        Collections.sort(bonds, comparator);

        for (JamesBond bond : bonds)
        {
            System.out.println(bond.getName() + " was born in " + bond.getYearOfBirth());
        }
    }
}

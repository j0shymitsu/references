package exercises;

import exercises.Classes.Employee;
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

        Employee vc = new Employee("Tim");
        Employee dean = new Employee("Garfield", vc);
        Employee headOfDept = new Employee("Linda", dean);
        Employee informaticsManager = new Employee("Adam", headOfDept);
        Employee developer = new Employee("Matt", informaticsManager);

        int managerCount = countLineManagement(developer);
        System.out.println(managerCount);
    }

    // structural recursion
    static int countLineManagement(Employee employee) {
        if (employee.getManager() == null) {
            return 0;
        }
        return 1 + countLineManagement(employee.getManager());
    }
}

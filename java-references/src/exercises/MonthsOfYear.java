package exercises;

import java.util.Scanner;

public class MonthsOfYear
{
    public static void main(String[] args) 
    {
        Scanner scanner = new Scanner(System.in);

        String[] monthsOfYear = {"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"};

        String fifthMonth = monthsOfYear[4];
        String indexEleven = monthsOfYear[11];

        System.out.println(fifthMonth);
        System.out.println(indexEleven);

        System.out.println("Enter the number of which month you want returned:");
        int userIndex = scanner.nextInt();
        System.out.println(returnMonth(userIndex));
    }   
    
    static String returnMonth(int month)
    {
        String[] monthsOfYear = {"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"};

        return monthsOfYear[month - 1];
    }
}

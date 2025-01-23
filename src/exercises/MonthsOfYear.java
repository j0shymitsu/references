public class MonthsOfYear 
{
    public static void main(String[] args) 
    {
        String[] monthsOfYear = {"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"};

        String fifthMonth = monthsOfYear[4];
        String indexEleven = monthsOfYear[11];

        System.out.println(fifthMonth);
        System.out.println(indexEleven);
    }   
    
    static String returnMonth(int month)
    {
        String[] monthsOfYear = {"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"};

        return monthsOfYear[month - 1];
    }
}

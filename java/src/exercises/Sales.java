package exercises;

public class Sales
{
    public static void main(String[] args)
    {
        // individual arrays takes the form [product id], [price in pence], [total number of sales]
        int[][] sales = {
                {1001, 1299, 14},
                {1002, 450, 50},
                {1003, 9999, 2},
                {1004, 200, 54}
        };

        int[] smallSales = new int[]{23, 65, 77, 12};

        /* Output the total sales for each product and test it works (values should be 18186, 22500, 19998, 10800) */

        for (int i = 0; i < sales.length; i++)
        {
            int productID = sales[i][0];
            int pricePence = sales[i][1];
            int numSales = sales[i][2];

            int totalSales = pricePence * numSales;
            System.out.println(totalSales);
        }


        /* Output the total for all sales, verify it works (value should be 71484) */

        int totalSales = 0;

        for (int i = 0; i < sales.length; i++)
        {
            totalSales += sales[i][1] * sales[i][2];
        }

        System.out.println("Total sales: " + totalSales);
        System.out.println();


        /* Refactor the code so you have a method that you can pass the 2D array into, and have the total value of all
         * sales returned. Run the programme to test it.
         */

        int total = totalSales(sales);
        System.out.println(total + "\n");


        /* Refactor again so you have another method can pass a one dimensional array in and get the total sales for
         * that product. Run the programme to test it.
         */

        int smallTotal = totalSales1D(smallSales);
        System.out.println(smallTotal);
    }

    static int totalSales(int[][] sales)
    {
        int totalSales = 0;

        for (int i = 0; i < sales.length; i++)
        {
            totalSales += sales[i][1] * sales[i][2];
        }

        System.out.println("Total sales: ");
        return totalSales;
    }

    static int totalSales1D(int[] sales)
    {
        int totalSales = 0;
        for (int i = 0; i < sales.length; i++)
        {
            totalSales += sales[i];
        }

        System.out.println("Total sales: ");
        return totalSales;
    }
}

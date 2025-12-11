package exercises;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class SalesTest
{

    @Test
    void totalSales()
    {
        // test when array is empty
        int[][] emptyArray = {};
        assertEquals(0, Sales.totalSales(emptyArray), "Total sales of an empty array should be 0.");

        // test with data
        int[][] sales = {
                {1001, 1299, 14},    // 18186
                {1002, 450, 50},     // 22500
                {1003, 9999, 2},     // 19998
                {1004, 200, 54},     // 10800
        };
        assertEquals(71484, Sales.totalSales(sales), "Total sales calculation is incorrect.");

        // test with zero sales
        int[][] noSales = {
                {1001, 1299, 0},
                {1002, 450, 0},
                {1003, 9999, 0},
                {1004, 200, 0}
        };
        assertEquals(0, Sales.totalSales(noSales), "Total sales should be 0 when all sales are 0.");
    }

    @Test
    void totalSales1D()
    {
        // test when array is empty
        int[] emptyArray = {};
        assertEquals(0, Sales.totalSales1D(emptyArray), "Total sales of an empty array should be 0.");

        // test with data
        int[] sales = {23, 65, 77, 12};    // 177
        assertEquals(177, Sales.totalSales1D(sales), "Total sales calculation incorrect. ");

        // test with 0
        int[] noSales = {0, 0, 0, 0};
        assertEquals(0, Sales.totalSales1D(noSales), "Total sales should be 0 when elements are 0.");
    }
}
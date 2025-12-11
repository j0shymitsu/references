package exercises;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class MonthsOfYearTest
{

    @Test
    void testReturnMonth()
    {
        assertEquals("January", MonthsOfYear.returnMonth(1), "Month 1 should be January");
        assertEquals("May", MonthsOfYear.returnMonth(5), "Month 5 should be May");
        assertEquals("December", MonthsOfYear.returnMonth(12), "Month 12 should be December");

        assertThrows(ArrayIndexOutOfBoundsException.class, () -> MonthsOfYear.returnMonth(0), "Month 0 should throw an exception");
        assertThrows(ArrayIndexOutOfBoundsException.class, () -> MonthsOfYear.returnMonth(13), "Month 13 should throw an exception");
    }
}
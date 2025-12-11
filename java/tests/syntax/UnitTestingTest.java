package syntax;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class UnitTestingTest {

    @Test
    void add()
    {
        int result2plus2 = UnitTesting.add(2, 2);
        assertEquals(4, result2plus2);    // expected; actual

        int result3plus7 = UnitTesting.add(3, 7);
        assertEquals(10, result3plus7);
    }
}
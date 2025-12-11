package exercises;

import org.junit.jupiter.api.Test;

import java.util.ArrayList;

import static org.junit.jupiter.api.Assertions.*;

class ZooNamesTest
{

    @Test
    public void testAddUniqueName()
    {
        // fresh list
        ArrayList<String> animalNames = new ArrayList<>();
        // unique name add
        ZooNames.isNameUnique(animalNames, "giraffe");
        // verify converted name is added
        assertTrue(animalNames.contains("GIRAFFE"), "GIRAFFE should be added to the list.");
        assertEquals(1, animalNames.size(), "List should have exactly one name after adding a unique name");
    }

    @Test
    public void testDupilcateNameNotAdded()
    {
        // fresh list
        ArrayList<String> animalNames = new ArrayList<>();
        ZooNames.isNameUnique(animalNames, "elephant");

        // attempt dupe
        ZooNames.isNameUnique(animalNames, "elephant");
        assertEquals(1, animalNames.size(), "Duplicate name should not be added to the list");
    }
}
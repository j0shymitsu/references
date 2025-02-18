package exercises;

import org.junit.jupiter.api.Test;

import java.util.ArrayList;

import static org.junit.jupiter.api.Assertions.*;

class SearchingArraysTest
{

    // test when list is empty
    @Test
    public void testEmptyList()
    {
        ArrayList<String> tweets = new ArrayList<>();
        ArrayList<String> result = SearchingArrays.fitsInTweet(tweets);
        assertNotNull(result, "Result should not be null");
        assertTrue(result.isEmpty(), "Result should be an empty list");
    }

    // test when tweets are valid
    @Test
    public void testValidTweet()
    {
        ArrayList<String> tweets = new ArrayList<>();
        tweets.add("hello, world!");
        tweets.add("This tweet is short");

        ArrayList<String> result = SearchingArrays.fitsInTweet(tweets);
        assertEquals(tweets.size(), result.size(), "All tweets should be valid");
        for (String tweet : tweets)
        {
            assertTrue(result.contains(tweet));
        }
    }
}
package exercises;

import java.util.ArrayList;

public class SearchingArrays
{
    public static void main(String[] args)
    {


    }

    static void multiplesOfTen()
    {
        ArrayList<Integer> intArrayList = new ArrayList<>();

        boolean arrayContainsMultipleOfTen = false;

        for (Integer i : intArrayList)
        {
            if (i % 10 == 0)
            {
                arrayContainsMultipleOfTen = true;
                break;
            }
        }
    }

    static void matchedWords()
    {
        ArrayList<String> stringArrayList = new ArrayList<>();
        ArrayList<String> matchedWords = new ArrayList<>();

        for (String word : stringArrayList)
        {
            if (word.startsWith("A"))
            {
                matchedWords.add(word);
            }
        }
    }

    public static ArrayList<String> fitsInTweet(ArrayList<String> tweets)
    {
        ArrayList<String> tweetableStrings = new ArrayList<>();

        for (String tweet : tweets)
        {
            if(tweet.length() <= 140)
            {
                tweetableStrings.add(tweet);
            }
        }

        return tweetableStrings;
    }

    public static ArrayList<Integer> numbersEndingWithValue(ArrayList<Integer> numberList, int endNumber)
    {
        ArrayList<Integer> result = new ArrayList<>();

        for (Integer num : numberList)
        {
            if (num % 10 == endNumber)
            {
                result.add(num);
            }
        }

        return result;
    }
}

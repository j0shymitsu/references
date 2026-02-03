package exercises;

import java.util.ArrayList;

public class InvalidTweetDeletion
{
    public static void main(String[] args)
    {

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
}

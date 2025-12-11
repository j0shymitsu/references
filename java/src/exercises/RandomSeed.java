package exercises;

import java.util.Random;

public class RandomSeed
{
    public static void main(String[] args)
    {
        int[] seeds = {1514626, 20956903, 2866};
        for (int i = 0; i < seeds.length; i++)
        {
            Random randomGenerator = new Random(seeds[i]);

            for (int j = 0; j < Math.max(3, String.valueOf(seeds[i]).length() - 2); j++)
            {
                System.out.println((char) (randomGenerator.nextInt(26) + 65));
            }
            System.out.println(i == 0 ? System.lineSeparator() : "");
        }
    }
}

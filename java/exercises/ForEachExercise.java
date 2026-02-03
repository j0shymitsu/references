package exercises;

public class ForEachExercise
{
    public static void main(String[] args)
    {
        String[] words = {"the", "cat", "sat", "on", "the", "mat"};
        String phrase = "";
        String phraseForEach = "";

        // for loop
        for (int i = 0; i < words.length; i++)
        {
            phrase += words[i] + " ";
        }
        System.out.println(phrase.trim());
        System.out.println();

        // for each loop
        for (String word : words)
        {
            phraseForEach += word + " ";
        }
        System.out.println(phraseForEach);
        System.out.println("\n\n");

        double total = 0;
        double totalForEach = 0;
        double[] hourlyTemperatures = {13.5, 14.5, 15.0, 15.5, 16.0, 16.5, 17.0, 17.5, 17.0, 16.0, 15.0, 14.0};

        // for loop
        for (int i = 0; i < hourlyTemperatures.length; i++)
        {
            total += hourlyTemperatures[i];
        }

        double average = total / hourlyTemperatures.length;
        System.out.println(average);

        // for each loop
        for (double hourlyTemperature : hourlyTemperatures)
        {
            totalForEach += hourlyTemperature;
        }

        double averageForEach = total / hourlyTemperatures.length;
        System.out.println(averageForEach);


    }
}

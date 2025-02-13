package exercises;

import java.util.Scanner;

public class MultipleChoice
{
    public static void main(String[] args)
    {
        Scanner inputScanner = new Scanner(System.in);

        String question = "";
        String[] answers = new String[4];
        int correctAnswer = 0;
        int userAnswer = 0;

        System.out.println("Please enter the question: ");
        question = inputScanner.nextLine();

        for (int i = 0; i < answers.length; i++)
        {
            int currentQuestion = i + 1;
            System.out.println("Please enter the answer for question " + currentQuestion + ":");
            answers[i] = inputScanner.nextLine();
        }

        System.out.println("Please enter the number of the correct answer: ");
        correctAnswer = inputScanner.nextInt();

        System.out.println("\nQuestions and answers saved!");
        System.out.println();

        while(true)
        {
            System.out.println("\n\n\n\n\n\n\n\n\n\n");
            System.out.println("Time to guess!\n");
            System.out.println("Question: " + question);
            System.out.println("Answers: ");

            for (int i = 0; i < answers.length; i++)
            {
                int answerNumber = i + 1;
                System.out.println(answerNumber + ". " + answers[i]);
            }

            System.out.println("\nEnter the number of your guess!");
            userAnswer = inputScanner.nextInt();

            if(userAnswer == correctAnswer)
            {
                System.out.println("Correct! The answer was number " + userAnswer);
                break;
            }
            else
            {
                System.out.println("Incorrect! The answer was number " + correctAnswer);
                break;
            }
        }
    }
}

package exercises;

import java.util.Scanner;

public class MultipleChoice
{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        String[] answers = new String[4];
        int correctAnswer = 0;

        System.out.println("Please enter your multiple choice question:");
        String userQuestion = scanner.nextLine();
        System.out.println("Please enter answer choice 1:");
        answers[0] = scanner.nextLine();
        System.out.println("Please enter answer choice 2:");
        answers[1] = scanner.nextLine();
        System.out.println("Please enter answer choice 3:");
        answers[2] = scanner.nextLine();
        System.out.println("Please enter answer choice 4:");
        answers[3] = scanner.nextLine();
        System.out.println("Please enter the number of the correct answer:");
        correctAnswer = scanner.nextInt();

        System.out.println("Please clear the terminal.");


    }
}

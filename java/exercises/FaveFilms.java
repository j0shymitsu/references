package exercises;

import java.util.Scanner;

public class FaveFilms
{
    public static void main(String[] args)
    {
        Scanner inputScanner = new Scanner(System.in);

        String[] faveFilms = new String[3];
        for (int i = 0; i < faveFilms.length; i++)
        {
            System.out.println("Please type (another) favourite film: ");
            String faveFilm = inputScanner.nextLine();
            faveFilms[i] = faveFilm;
        }

        System.out.println("\nYour favourite films are:");
        for (int i = 0; i < faveFilms.length; i++)
        {
            System.out.println(faveFilms[i]);
        }
    }
}

public class Scanner
{
    public static void main(String[] args) 
    {
        System.out.println("Please type your name:");

        java.util.Scanner inputScanner = new java.util.Scanner(System.in);

        String userName = inputScanner.nextLine();

        String greeting = "Hello " + userName;

        System.out.println(greeting);
    }
}

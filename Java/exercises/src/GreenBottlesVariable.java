public class GreenBottlesVariable 
{
    public static void main(String[] args) 
    {
        int noOfBottles = 10;
        String wallPhrase = " green bottles hanging on the wall";

        while(noOfBottles > 0)
        {
        System.out.print(noOfBottles + wallPhrase + ",\n");
        System.out.print(noOfBottles + wallPhrase + ",\n");
        System.out.print("And if one green bottle should \"accidentally\" fall, there'd be ");
        noOfBottles -= 1;
        System.out.print(noOfBottles + wallPhrase);
        System.out.println("\n");
        }
    }
}

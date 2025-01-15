public class Array
{
    public static void main(String[] args) 
    {

        /* - Types can't be mixed
           - Don't declare array on variable (in C style)
        */

        int[] marks = new int[]{23, 65, 77, 12};
        int secondMark = marks[1];

        String[] names = new String[]{"Josh", "Java", "Python", "Ruby", "Haskell"};    // Array literal
        names[3] = "Golang";
        String lastName = names[4];

        System.out.println(secondMark);
        System.out.println(lastName);
        System.out.println(names[3]);
        
    }
}

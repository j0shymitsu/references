public class Concatenation 
{
    public static void main(String[] args) 
    {
        String birthdayPerson = "\"Java\"\n";
        String songLine = "Happy birthday to you\n";
        String song = songLine + songLine + "Happy birthday dear " + birthdayPerson + songLine;
        
        System.out.println(song);

        song += songLine;

        System.out.println(song);
    }    
}

public class Happy 
{
    public static void main(String[] args) 
    {
        String happy = "If you're happy and you know it ";
        String action = "clap your hands!\n";
        String line = happy + action;
        String verse = line;
        verse += line;
        verse += happy + "and you really want to show it,\n";
        verse += line;
        
        System.out.println();
        System.out.print(verse);    

        action = "stomp your feet!";

        System.out.println();
        System.out.print(happy);
        System.out.print(action + "\n");
        System.out.print(happy);
        System.out.print(action + "\n");
        System.out.print(happy);
        System.out.print("and you really want to show it, " + "\n");
        System.out.print(happy);
        System.out.print(action + "\n");
    }    
}

package syntax.classes;

public class Main
{
    public static void main(String[] args)
    {
        Module programmingI = new Module("CO4225", "Programming I");
        Module innovationProject = new Module("CO6008", "Innovation Project", 40);

        String moduleCode = programmingI.getCode();
        int level = programmingI.getLevel();
        int innovationProjectCredits = innovationProject.getCredits();

        System.out.println(moduleCode);
        System.out.println(level);
        System.out.println(innovationProjectCredits);
    }

}

package exercises;

import java.util.Random;

public class PokeTutor
{
    private String name;
    private int combatPoints;
    private double fleeRate;

    // constructor
    public PokeTutor(String name, int maxCombatPoints, double fleeRate)
    {
        this.name = name.trim();
        this.fleeRate = fleeRate;

        // randomly allocate a cp value up to max
        Random randomGenerator = new Random();
        final int randomCP = randomGenerator.nextInt(maxCombatPoints);
        this.combatPoints = Math.max(10, randomCP);    // use math max method to ensure cp !<10
    }

    // getters
    public String getName()
    {
        return name;
    }

    public int getCombatPoints()
    {
        return combatPoints;
    }

    private double getEscapeChance(PokeBall ball)
    {
        double escapeChance = combatPoints / 1000.0;    // max cp will be 1000
        switch (ball)
        {
            case GREAT:
                escapeChance *= 0.66666;
                break;
            case ULTRA:
                escapeChance *= 0.33333;
        }
        return escapeChance;
    }

    // setters

    // methods
    enum CaptureResult
    {
        FAIL, FLEE, CAUGHT
    }

    private boolean shouldFlee()
    {
        Random random = new Random();
        boolean flee = random.nextDouble() < fleeRate;
        return flee;
    }

    CaptureResult attemptCapture(PokeBall ball)
    {
        final double escapeChance = getEscapeChance(ball);
        Random random = new Random();
        final double chance = random.nextDouble();
        if (chance > escapeChance)
        {
            return CaptureResult.CAUGHT;
        }
        // will only get this far if not caught
        if(shouldFlee())
        {
            return CaptureResult.FLEE;
        }
        else
        {
            return CaptureResult.FAIL;
        }
    }

}

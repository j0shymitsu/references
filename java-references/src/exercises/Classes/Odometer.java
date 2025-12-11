package exercises.Classes;

public class Odometer
{
    static final String KILOMETERS = "kilometers";
    static final String MILES = "miles";
    static final String NAUTICAL_MILES = "nauticalMiles";

    private double totalMilesTravelled;
    private DistanceUnit displayUnits = DistanceUnit.MILES;

    // Constructor
    public Odometer()
    {
        totalMilesTravelled = 0;
    }

    public Odometer(double startMileage)
    {
        totalMilesTravelled = startMileage;
    }


    // Getters
    public double getTotalMilesTravelled()
    {
        return totalMilesTravelled;
    }

    public double getTotalDistanceTravelled()
    {
        return switch (displayUnits)
        {
            case KILOMETERS -> totalMilesTravelled * 1.60934;
            case NAUTICAL_MILES -> totalMilesTravelled * 0.868976;
            case MILES -> totalMilesTravelled;
            default -> 0;    // never be reached unless the enum is modified
        };
    }

    // Methods
    public void addMileage(double miles)
    {
        totalMilesTravelled += miles;
    }

    public double addTrip(double miles)
    {
        totalMilesTravelled += miles;

        System.out.println("New total mileage:\n" + totalMilesTravelled);
        System.out.println("\nMileage this trip:");
        return miles;
    }

    public void setDisplayUnits(DistanceUnit displayUnits)
    {
        this.displayUnits = displayUnits;
    }

    @Override
    public String toString()
    {
        return "Odometer " + Double.toString(totalMilesTravelled);
    }
}

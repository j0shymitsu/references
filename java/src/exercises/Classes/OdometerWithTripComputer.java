package exercises.Classes;

import java.nio.file.Paths;

public class OdometerWithTripComputer extends Odometer
{
    private double tripStartMileage = 0;

    public OdometerWithTripComputer(double startMileage)
    {
        super(startMileage);
        tripStartMileage = startMileage;
    }
    public void resetTripCounter()
    {
        tripStartMileage = getTotalMilesTravelled();
    }

    public double currentTripMileage()
    {
        return getTotalMilesTravelled() - tripStartMileage;
    }

    @Override
    public String toString()
    {
        return "Class: " + getClass() + "\nTotal Mileage: " + getTotalMilesTravelled() + "\nTrip Mileage: " +
                getTotalDistanceTravelled();
    }
}

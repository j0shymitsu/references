package exercises.Classes;

public class AdvancedTripComputer extends OdometerWithTripComputer
{
    private double fuelUsedSinceReset = 0;

    public AdvancedTripComputer(double startMileage)
    {
        super(startMileage);
    }

    public void resetTripComputer()    // resets both trip mileage and fuel usage
    {
        super.resetTripCounter();
        fuelUsedSinceReset = 0;
    }

    public void addFuelUsed(double gallons)
    {
        if (gallons < 0)
        {
            throw new IllegalArgumentException("Gallons cannot be negative.");
        }
        fuelUsedSinceReset += gallons;
    }

    public double calculateMPG()
    {
        if (fuelUsedSinceReset == 0)
        {
            return 0;
        }
        return currentTripMileage() / fuelUsedSinceReset;
    }

    public double getFuelUsedSinceReset()
    {
        return fuelUsedSinceReset;
    }
}

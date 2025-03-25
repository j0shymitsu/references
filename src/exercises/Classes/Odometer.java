package exercises.Classes;

public class Odometer
{
    private double totalMilesTravelled;

    // Constructor
    public Odometer()
    {
        totalMilesTravelled = 0;
    }

    // Getters
    public double getTotalMilesTravelled()
    {
        return totalMilesTravelled;
    }

    // Methods
    public void addMileage(double miles)
    {
        totalMilesTravelled += miles;
    }
}

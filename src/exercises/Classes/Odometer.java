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

    public double addTrip(double miles)
    {
        double thisTrip = miles;
        totalMilesTravelled += miles;

        System.out.println("New total mileage:\n" + totalMilesTravelled);
        System.out.println("\nMileage this trip:");
        return thisTrip;
    }
}

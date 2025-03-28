package exercises.Classes;

public class Main
{
    public static void main(String[] args)
    {
        Odometer odo = new Odometer();
        odo.addMileage(123.4);
        System.out.println("Mileage so far: ");
        System.out.println(odo.getTotalMilesTravelled());    // 123.4
        odo.addMileage(56.5);
        System.out.println("Mileage now: ");
        System.out.println(odo.getTotalMilesTravelled());    // 179.9
        System.out.println();

        // Tasks
        Odometer odoTwo = new Odometer();
        odoTwo.addMileage(2.25);
        odoTwo.addMileage(17.75);
        System.out.println("Mileage: ");
        System.out.println(odoTwo.getTotalMilesTravelled());
        System.out.println();
        odoTwo.addTrip(24);
    }
}

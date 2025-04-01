package exercises.Classes;

import java.time.LocalDateTime;

public class Main
{
    public static void main(String[] args)
    {
        LocalDateTime dateTime = LocalDateTime.of(2025, 04, 01, 14, 30);
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

        // Enums
        Odometer odoThree = new Odometer();
        odoThree.setDisplayUnits(DistanceUnit.KILOMETERS);
        odoThree.addMileage(5);
        double distance = odoThree.getTotalDistanceTravelled();
        System.out.println(distance + "\n");


        Meeting meetingOne = new Meeting("Chester", dateTime, 30.00, "Meeting");
        meetingOne.setState(State.BUSY);
    }
}

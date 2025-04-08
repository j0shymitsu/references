package exercises.Classes;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

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

        // TripComputer (inheritance)
        OdometerWithTripComputer tripComputer = new OdometerWithTripComputer(0);
        tripComputer.addMileage(148.32);
        System.out.println("Total mileage: " + tripComputer.getTotalMilesTravelled());
        System.out.println("Trip mileage: " + tripComputer.currentTripMileage());
        tripComputer.resetTripCounter();
        tripComputer.addMileage(217.16);
        System.out.println("Total mileage: " + tripComputer.getTotalMilesTravelled());
        System.out.println("Trip mileage:" + tripComputer.currentTripMileage());
        System.out.println();

        AdvancedTripComputer advancedTripComputer = new AdvancedTripComputer(190);
        advancedTripComputer.addMileage(120);
        advancedTripComputer.addFuelUsed(2.1);
        advancedTripComputer.calculateMPG();
        System.out.println(advancedTripComputer.calculateMPG());
        System.out.println();

        // Overrides
        System.out.println(odo);    // implicitly calls odo.ToString()
        System.out.println();
        System.out.println(tripComputer);    // Task (as above)
        System.out.println(meetingOne);
        System.out.println();

        // method overloading
        HomeAppliance appliance = new HomeAppliance();
        describe(appliance);

        Kettle kettle = new Kettle();
        describe(kettle);
        kettle.boil();

        HomeAppliance newKettle = new Kettle();
        describe(kettle);
        kettle.boil();

        System.out.println();

        ArrayList<HomeAppliance> appliances = new ArrayList<>();
        appliances.add(appliance);
        appliances.add(kettle);

        for (HomeAppliance someAppliance : appliances)
        {
            someAppliance.describe();    // implement like this for overrides
        }
        System.out.println();


        //

        Animal bird = new Animal();
        Dog dog = new Dog();

        List<Animal> animals = new ArrayList<>();
        animals.add(bird);
        animals.add(dog);

        for (Animal animal : animals)
        {
            describe(animal);
        }
    }

    // method overloading
    static void describe(HomeAppliance appliance)
    {
        System.out.println("This is a home appliance");
    }

    static void describe(Kettle kettle)
    {
        System.out.println("This is a kettle");
    }

    static void describe(Animal animal)
    {
        System.out.println("An animal");
    }

    static void describe(Dog dog)
    {
        System.out.println("A dog");
    }
}

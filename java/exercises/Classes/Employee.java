package exercises.Classes;

public class Employee {
    private String name;
    private Employee manager;

    public Employee(String name, Employee manager) {
        this.name = name;
        this.manager = manager;
    }

    public Employee(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public Employee getManager() {
        return manager;
    }
}

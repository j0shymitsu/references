package syntax.Classes;

import java.util.Date;

public class Employee
{
    private String forename;
    private String surname;
    private Date startDate;

    // constructor
    public Employee(String forename, String surname, Date startDate)
    {
        this.forename = forename;
        this.surname = surname;
        this.startDate = startDate;
    }

    // getters
    public String getForename()
    {
        return forename;
    }

    public String getSurname()
    {
        return surname;
    }

    public Date getStartDate()
    {
        return startDate;
    }

    // setters
    public void setForename(String forename)
    {
        this.forename = forename;
    }

    public void setSurname(String surname)
    {
        this.surname = surname;
    }
}

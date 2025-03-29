package exercises.Classes;

import java.time.LocalDate;
import java.time.LocalDateTime;

public class Meeting
{
    private String location;
    private LocalDateTime startTime;
    private double duration;
    private String notes;

    // Constructor
    public Meeting(String location, LocalDateTime startTime, double duration, String notes)
    {
        this.location = location;
        this.startTime = startTime;
        this.duration = duration;
        this.notes = notes;
    }

    // Getters
    public String getLocation()
    {
        return location;
    }

    public LocalDateTime getStartTime()
    {
        return startTime;
    }

    public double getDuration()
    {
        return duration;
    }

    public String getNotes()
    {
        return notes;
    }

    // Setters
    public void setStartTime(int days)
    {
        LocalDateTime newDate = LocalDateTime.from(startTime.plusDays(days));
        startTime = newDate;
    }

    // Methods
    public double extendMeeting(double extraHours)
    {
        if(duration != 0)
        {
            duration += extraHours;
        }

        return duration;
    }

}

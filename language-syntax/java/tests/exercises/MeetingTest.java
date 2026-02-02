package exercises;

import exercises.Classes.Meeting;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.time.LocalDateTime;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class MeetingTest
{
    private Meeting meeting;
    private LocalDateTime originalTime;

    @BeforeEach
    public void setUp()
    {
        originalTime = LocalDateTime.of(2025, 3, 29, 9, 25);    /* 29 march 2025,
        2pm */
        meeting = new Meeting("London", originalTime, 2.0, "Overview");
    }

    @Test
    public void testExtendMeeting()
    {
        double newDuration = meeting.extendMeeting(1.5);
        assertEquals(3.5, newDuration, 0.001);
    }

    @Test
    public void testExtendMeetingZeroInitialDuration()
    {
        Meeting zeroDurationMeeting = new Meeting("Teams", originalTime, 0.0, "Catch-up");
        double result = zeroDurationMeeting.extendMeeting(1.0);
        assertEquals(0.0, result, 0.001);
    }

    @Test
    public void testRescheduleMeeting()
    {
        meeting.setStartTime(3);    // move forward 3 days
        LocalDateTime expectedTime = originalTime.plusDays(3);
        assertEquals(expectedTime, meeting.getStartTime());
    }

    @Test
    public void testInitialValues()
    {
        assertEquals("London", meeting.getLocation());
        assertEquals(originalTime, meeting.getStartTime());
        assertEquals(2.0, meeting.getDuration(), 0.001);
        assertEquals("Overview", meeting.getNotes());
    }
}

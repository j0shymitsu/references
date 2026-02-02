import math
import datetime as dt



#################
### DATE/TIME ###
#################



# Current date
currentDate = dt.date.today()
timeOnly = dt.datetime.now().time()
dt_a = dt.datetime.now()

print(f"Current date is: {currentDate.strftime('%d/%m/%Y')}") 
print(f"Current year is: {dt_a.strftime('%Y')}")
print(f"Current month is: {dt_a.strftime('%m, %b')}")
print(f"Current time is: {timeOnly}")
print(f"Current dt is: {dt_a}")
print()

# Input date and display in x format
strDate = input("Enter a date (DD/MM/YYYY): ")
year = int(strDate[6:10]) # Converting the string input to integer; displaying index 6 through 10.
month = int(strDate[3:5])
day = int(strDate[0:2])
myDate = dt.datetime(year, month, day)

print(myDate)
print(f"Formatted date is: {myDate.strftime('%Y/%m/%d')}") # Displaying as (YYYY/MM/DD).  # "strftime" - Object that returns a string representing the date, formatted according to specified.
print(f"Another formatted date is: {myDate.strftime('%d-%b-%y')}") # Displaying as (DD-Mon-YY).
print(f"Another formatted date is: {myDate.strftime('%a %b %d, %Y')}") # Displaying as (Day Mon DD, YYYY)
print()

# Calculate how many days from now until Christmas
print(f"Days from today until Christmas is: ", dt.datetime(2024, 12, 25) - dt.datetime.today())
print()

# Calculate how old I am
myBday = input("Please enter your birthday (DD/MM/YYYY): ")
myYear = int(myBday[6:10])
myMonth = int(myBday[3:5])
myDay = int(myBday[0:2])
myBirthdate = dt.datetime(myYear, myMonth, myDay)

td = dt_a - myBirthdate
days = td.days
totalSeconds = td.total_seconds() # Calculats total number of seconds; must be calculated as seconds first then converted.
hours, remainder = divmod(totalSeconds, 3600)
minutes, seconds = divmod(remainder, 60)

age = f"{days} days, or; {int(hours)} hours, {int(minutes)} minutes and {int(seconds)} seconds."

print(f"Your age is: {age}")   
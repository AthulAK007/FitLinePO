import calendar
from datetime import datetime

def get_valid_dates():
    # Get the current year and month
    now = datetime.now()
    year = now.year
    month = now.month + 3
    
    # Adjust year if month exceeds December
    if month > 12:
        year += 1
        month -= 12
    
    # Get the calendar matrix for the specified month
    month_calendar = calendar.monthcalendar(year, month)
    
    # Store the valid dates in a list, excluding Saturdays, Sundays, Mondays, and specified dates
    valid_dates = []
    
    # Find the index of the first Monday in the month
    first_monday_index = next((i for i, day in enumerate(month_calendar) if day[calendar.MONDAY] != 0), -1)
    
    if first_monday_index == -1:
        return valid_dates  # No complete week starting from Monday
    
    # Append the valid dates for the first three full weeks starting from Monday to the list
    for week in month_calendar[first_monday_index:first_monday_index+3]:
        for day in week:
            if day != 0 and calendar.weekday(year, month, day) not in [0, 4, 5, 6]:  # Exclude Mondays, Fridays, Saturdays, and Sundays
                # Check if the date is not in the excluded list
                if not is_excluded_date(day, month):
                    # Get the day of the week number (1 for Monday, 2 for Tuesday, etc.)
                    day_of_week = calendar.weekday(year, month, day) + 1
                    valid_dates.append(f"{day:02d}/{month:02d}/{year}/{day_of_week}")
    
    return valid_dates

def is_excluded_date(day, month):
    # List of excluded dates (day/month)
    excluded_dates = [
        (1, 1),
        (6, 1),
        (29,3),
        (1,4),
        (1,5),
        (9,5),
        (20,5),
        (30,5),
        (3,10),
        (31,10),
        (1,11),
        (24,12),
        (25, 12),
        (26,12),
        (27,12),
        (28,12),
        (29,12),
        (30,12),
        (31,12),
        (1,1),
        (2,1)
    ]
    return (day, month) in excluded_dates

# Example usage
#valid_dates = get_valid_dates()
#print("Valid Dates for May (excluding Mondays, Fridays, Saturdays, Sundays, and specified dates):")
#for date in valid_dates:
#    print(date)

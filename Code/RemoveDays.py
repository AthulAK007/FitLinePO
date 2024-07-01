import calendar
from datetime import datetime

def get_valid_dates(varcount_str):
    # Convert varcount_str to an integer
    varcount = int(varcount_str)
    
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
    
    # Count the number of valid dates
    count = len(valid_dates)
    
    # Define a function to extract the last day from the date
    def get_last_day(date_string):
        return int(date_string.split('/')[-1])

    # Sort the valid dates based on the last day
    valid_dates.sort(key=get_last_day)

    # Prepare the list of dates to return
    dates_to_return = []
    
    if varcount == 2 and count >= 3:
        dates_to_return.append(valid_dates[0])  # Add the first date
        dates_to_return.append(valid_dates[2])  # Add the third date
    else:
        repetitions = varcount // count
        remainder = varcount % count

        for i in range(repetitions):
            dates_to_return.extend(valid_dates)
        
        dates_to_return.extend(valid_dates[:remainder])

    return dates_to_return

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
#varcount_str = "2"  # Specify the number of dates you want as a string
#returned_dates = get_valid_dates(varcount_str)
#for date in returned_dates:
#    print(date)

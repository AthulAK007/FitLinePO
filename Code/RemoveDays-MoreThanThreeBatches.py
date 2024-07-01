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
    
    # Store the valid dates in a list, excluding Saturdays, Sundays, and Mondays
    valid_dates = []
    for i in range(6):  # Include the current month + 5 additional months
        # Calculate the year and month for the current iteration
        curr_year = year if month + i <= 12 else year + 1
        curr_month = (month + i) % 12 if month + i <= 12 else (month + i) % 12 or 12
        
        # Get the calendar matrix for the current month
        month_calendar = calendar.monthcalendar(curr_year, curr_month)
        
        # Calculate the total number of weeks in the month
        total_weeks = len(month_calendar)
        
        # Check if the last week contains any days from the next month
        for day in month_calendar[-1]:
            if day != 0 and day > 7:
                total_weeks -= 1  # Exclude the last week
                break
        
        # Count the number of non-zero days in the last week
        last_week_non_zero_count = sum(1 for day in month_calendar[-1] if day != 0)
        
        # If the count of non-zero days in the last week is less than 4,
        # remove both the last week and the second-to-last week
        if last_week_non_zero_count < 4:
            total_weeks -= 1  # Exclude the second-to-last week as well
        
        # Append the valid dates for the current month to the list
        for week in month_calendar[:total_weeks]:
            for day in week:
                if day != 0 and calendar.weekday(curr_year, curr_month, day) not in [5, 6, 0]:
                    # Get the day of the week number (1 for Monday, 2 for Tuesday, etc.)
                    day_of_week = calendar.weekday(curr_year, curr_month, day) + 1
                    valid_dates.append(f"{day:02d}/{curr_month:02d}/{curr_year}/{day_of_week}")
    
    return valid_dates

# Example usage
#valid_dates = get_valid_dates()
#print("Valid Dates (excluding Saturdays, Sundays, and Mondays):")
#for date in valid_dates:
#    print(date)

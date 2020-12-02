# Import datetime format
from datetime import datetime

# Input if year is leap or not
leap_year = int(input())
# Source: day of the week, month and day
[source_day_week,source_month,source_day] = input().split()
source_day = int(source_day)
# Target: month and day
[target_month,target_day] = input().split()
target_day = int(target_day)

# Dictionaries with number and month/day of the week
months = {1:"Jan",2:"Feb",3:"Mar",4:"Apr",5:"May",6:"Jun",7:"Jul",8:"Aug",9:"Sep",10:"Oct",11:"Nov",12:"Dec"}
weeks = {1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday",7:"Sunday"}

# Number for day of the week of source
source_day_week = list(weeks.keys())[list(weeks.values()).index(source_day_week)]
# Number of month for source and target
source_month = list(months.keys())[list(months.values()).index(source_month)]
target_month = list(months.keys())[list(months.values()).index(target_month)]

# If both dates are in the same month
if source_month == target_month:
    # The first and last month are the same
    first = source_month
    last = target_month
    # If the target day is after the source
    if target_day > source_day:
        # The first one is the source
        first_day = source_day
        last_day = target_day
    # Otherwise
    else:
        # The first one is the target
        first_day = target_day
        last_day = source_day
# If the source month is before the target month
elif source_month < target_month:
    # The first day and month are the source
    first = source_month
    first_day = source_day
    last = target_month
    last_day = target_day
# Otherwise
else:
    # The first day and month are the target
    first = target_month
    first_day = target_day
    last = source_month
    last_day = source_day

# If it is a leap year, use 2020 as a year example
if leap_year == 1:
    year = 2020
# Otherwise, use 2019
else:
    year = 2019

# Obtain the difference in days for the two dates providad
diff = (datetime(year,last,last_day) - datetime(year,first,first_day)).days
# Module with 7 to obtain the difference in a week in days (between 0 and 6 included)
diff_week = diff % 7

# If the month is the same
if source_month == target_month:
    # If the target goes after the source
    if target_day > source_day:
        # Sum the difference to the source day of the week
        day_of_week = source_day_week + diff_week
        # If it is over 7, decrease the result
        if day_of_week > 7:
            day_of_week -= 7
    # Otherwise
    else:
        # Substract the difference to the source day of the week
        day_of_week = source_day_week - diff_week
        # If it is below 1, increase the result
        if day_of_week < 1:
            day_of_week += 7
# If the source goes before the target
elif source_month < target_month:
    # Sum the difference to the source day of the week
    day_of_week = source_day_week + diff_week
    # If it is over 7, decrease the result
    if day_of_week > 7:
        day_of_week -= 7
# Otherwise
else:
    # Substract the difference to the source day of the week
    day_of_week = source_day_week - diff_week
    # If it is below 1, increase the result
    if day_of_week < 1:
        day_of_week += 7    

# Print the name of the resulting day of the week
print(weeks[day_of_week])

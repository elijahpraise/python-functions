from datetime import datetime, timedelta

# String with full day and month name
date_str = "Wednesday,10 February,2021 12:19:47"

# %A is to parse weekday and %B to parse month name
dt_obj = datetime.strptime(date_str, "%A,%d %B,%Y %H:%M:%S")
result = dt_obj + timedelta(hours=37, minutes=11, seconds=3)
print("Date Object:", dt_obj)
print(result, 'this is it......................')
# Output  2021-02-10 12:19:47

result = datetime.strptime('Tuesday', "%A")
print(result.weekday())
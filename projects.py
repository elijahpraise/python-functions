from datetime import datetime, timedelta


def add_time(start, duration, day=None):
    """

    :param start:
    :param duration:
    :param day:
    :return:
    """
    if day is not None:
        date_strings = {
            'monday': f'Monday,1 February,2021 {start}', 'tuesday': f'Tuesday,1 February,2022 {start}',
            'wednesday': f'Wednesday,2 February,2022 {start}',
            'thursday': f'Thursday, 3 February,2022 {start}', 'friday': f'Friday,4 February,2022 {start}',
            f'saturday': f'Saturday,5 February,2022 {start}', 'sunday': f'Sunday,6 February,2022 {start}'
        }
        start_day = date_strings.get(day.lower())
        result = datetime.strptime(start_day, "%A,%d %B,%Y %I:%M %p")
    else:
        result = datetime.strptime(start, "%I:%M %p")
    duration = duration.split(":")
    hours = int(duration[0])
    minutes = int(duration[1])
    later_time = (result + timedelta(hours=hours, minutes=minutes))
    days_later = later_time.day - 1
    if day is not None:
        formatted_datetime = later_time.strftime("%I:%M %p %A")
    else:
        formatted_datetime = later_time.strftime("%I:%M %p")
    return_string = "# Returns:"
    if days_later == 0:
        return f"{return_string} {formatted_datetime}"
    elif days_later == 1:
        return f'{return_string} {formatted_datetime} (next day)'
    else:
        return f'{return_string} {formatted_datetime} ({days_later} days later)'


print(add_time("6:30 PM", "205:12"))

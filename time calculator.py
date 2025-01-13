def add_time(start, duration, start_day=""):
    if start.endswith('PM'):
        twenty_four_hour=str(int(start[:-6]) + 12) + ':' + start[-5:-3] #it is a string

    else:
        twenty_four_hour=start[:-3] #it is a string

    #converting duration and start into hours
    duration_hours=(int(duration[-2:]) / 60) + int(duration[:-3])
    days=int(duration_hours//24)
    hours=((duration_hours/24) - days) * 24
    start_hours=(int(twenty_four_hour[-2:]) / 60) + int(twenty_four_hour[:-3])

    #add duration hours to start hours
    day_time=start_hours+hours

    if day_time>24:
        day_time=day_time-24
        days+=1
    day_time_hour=int(day_time)
    day_time_minutes=int(round(((day_time-int(day_time)) * 60), 0))
    if day_time_minutes==60:
        day_time_hour+=1
        day_time_minutes=0
    final_time_minutes = str(day_time_minutes).zfill(2)
    final_time_hour = str(day_time_hour).zfill(2)
    if day_time_hour>12:
        day_time_hour=day_time_hour-12
        final_time_hour= str(day_time_hour).zfill(2)
        final_time=final_time_hour + ":" + final_time_minutes + " " + "PM"
    elif day_time_hour== 12:
        final_time = final_time_hour + ":" + final_time_minutes + " " +"PM"
    elif day_time_hour==0:
        final_time = str(int(final_time_hour)+12) + ":" + final_time_minutes + " " + "AM"
    else:
        final_time = final_time_hour + ":" + final_time_minutes + " " + "AM"
    #return final_time
#done with the time and days(days) now add days of the week
    days_of_the_week=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if  not start_day:
        if days==0:
            new_time=final_time
        elif days==1:
            new_time = final_time + " " + "(next day)"
        else:
            new_time= final_time + " " + f"({days} days later)"
    else:
        index_of_days_of_the_week = (days_of_the_week.index(start_day.lower().capitalize()) + days) % len(days_of_the_week)
        if days==0:
            new_time=final_time + "," + " " + start_day
        elif days==1:
            new_time = final_time + "," + " " + days_of_the_week[index_of_days_of_the_week] + " " + "(next day)"
        else:
            new_time = final_time + "," + " " + days_of_the_week[index_of_days_of_the_week] + " " + f"({days} days later)"
    return new_time


print(add_time('2:59 AM', '24:00', 'saturDay'))
from datetime import datetime

def augmentColummnWiseDataWithDateAndTime(incident):

    date = incident["date_time"].split(" ")[0] 

    dayOfWeek = datetime.strptime(date, '%m/%d/%Y').isoweekday() % 7
    dayOfWeekAdjusted = dayOfWeek + 1 if dayOfWeek < 7 else 1

    time = incident["date_time"].split(" ")[1]
    hour = time.split(":")[0]

    incident["day"]= dayOfWeekAdjusted 
    incident["hour"] = hour 
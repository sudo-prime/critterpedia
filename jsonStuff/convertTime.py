#!/usr/bin/env python3

import re

def toMilTime(hours):
    #If PM, add 12 for military time
    #This function will not work if either time is noon or midnight
    #But that edgecase does not exist here, so its k
    milHour = 0

    hour = hours.split()
    if hour[1] == 'p':
        milHour = int(hour[0]) + 12
    else:
        milHour = int(hour[0])

    return milHour

def setHours(start, end, hours):
    hourIter = start

    while hourIter != end:
        if hourIter == 24:
            hourIter = 0
        
        hours[hourIter] = 1
        hourIter += 1

    hours[end] = 1
    return hours


def convertTime(time):
    hours = {}

    if time == "All day":
        for hour in range(0,24):
            hours[hour]=1
        return hours

    for hour in range(0,24):
        hours[hour]=0

    times = re.findall(r'\d{1,2} [a|p]', time)

    milHours = []

    for time in times:
        milHours.append(toMilTime(time))
    
    hours = setHours(milHours[0], milHours[1], hours)
    if (len(milHours) == 4):
        hours = setHours(milHours[2], milHours[3], hours)

    return hours

#print(convertTime("6 p.m. - 4 a.m."))
#print(convertTime("All day"))
#print(convertTime("9 a.m. - 4 p.m., 9 p.m. - 4 a.m."))

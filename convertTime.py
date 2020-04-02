#!/usr/bin/env python3

import re

def toMilTime(hours):
    #Splits the two times into their own arrays for easy iteration
    split = [hours[0:2], hours[2:4]]
    milHours=[]

    #If PM, add 12 for military time
    #This function will not work if either time is noon or midnight
    #But that edgecase does not exist here, so its k
    for time in split:
        if time[1] == 'p':
            time[0] = int(time[0]) + 12
        else:
            time[0] = int(time[0])
        milHours.append(time[0])
    return milHours

def convertTime(time):
    hours = {}

    if time == "All day":
        for hour in range(0,24):
            hours[hour]=1
        return hours

    times = re.findall(r'([\d|a|p])', time)
    milTimes = toMilTime(times)
    
    for hour in range(0,24):
        hours[hour]=0

    hour = milTimes[0]

    while hour != milTimes[1]:
        if hour == 24:
            hour = 0
        
        hours[hour] = 1
        hour += 1
    
    hours[milTimes[1]] = 1

    return hours


#print(convertTime("6 p.m. - 4 a.m."))
#print(convertTime("All day"))
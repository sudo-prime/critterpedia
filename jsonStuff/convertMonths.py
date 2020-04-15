#!/usr/bin/env python3

import re
import calendar

ALLMONTHS = calendar.month_name
monthTable = {}

currentMonth = 1

for month in ALLMONTHS[1:13]:
    monthTable[month] = currentMonth
    currentMonth += 1

def monthNametoNum(month):
    return monthTable[month]

def setMonths(start, end, monthData):
    #Sets all months from start to end in monthdata to 1 and returns monthdata
    monthIter = start

    while monthIter != end:
        if monthIter == 13:
            monthIter = 1
        
        monthData[monthIter] = 1
        monthIter += 1

    monthData[end] = 1
    return monthData

def convertMonths(months):
    monthData = {}

    if months == 'Year-round (Northern and Southern)':
        for month in range(1,13):
            monthData[month]=1
        return monthData
    
    for month in range(1,13):
        monthData[month] = 0
    
    months = re.sub(r'(.*?) \(.*?$', r'\g<1>', months)
    monthRange = re.findall(r'\w+', months)

    monthRangeNums = []

    for monthName in monthRange:
        monthRangeNums.append(monthNametoNum(monthName))

    if(len(monthRangeNums) == 1):
        monthData = setMonths(monthRangeNums[0], monthRangeNums[0], monthData)
    
    elif(len(monthRangeNums) == 4):
        monthData = setMonths(monthRangeNums[0], monthRangeNums[1], monthData)
        monthData = setMonths(monthRangeNums[2], monthRangeNums[3], monthData)
    
    else:
        monthData = setMonths(monthRangeNums[0], monthRangeNums[1], monthData)

    return monthData

#Test Cases
#print(convertMonths('November-March (Northern) / May-September (Southern)'))
#print(convertMonths('Year-round (Northern and Southern)'))
#print(convertMonths('September (Northern) / March (Southern)'))
#print(convertMonths('March-June, September-October (Northern) / March-April, September-December (Southern)'))
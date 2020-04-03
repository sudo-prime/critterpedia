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


def convertMonths(months):
    monthData = {}
    print(months)

    if months == 'Year-round (Northern and Southern)':
        for month in range(1,13):
            monthData[month]=1
        return monthData
    
    months = re.sub(r'(\w*\-\w*).*?$', r'\g<1>', months)
    monthRange = re.findall(r'\w+', months)

    monthRange[0] = monthNametoNum(monthRange[0])

    #Fix error that occurs with Salmon and King Salmon only being available one month
    try:
        monthRange[1] = monthNametoNum(monthRange[1])
    except:
        monthRange[1] = monthRange[0]

    for month in range(1,13):
        monthData[month] = 0
        
    monthIter = monthRange[0]

    while monthIter != monthRange[1]:
        if monthIter == 13:
            monthIter = 1
        
        monthData[monthIter] = 1
        monthIter += 1

    monthData[monthRange[1]] = 1
    return monthData

#Test Cases
#print(convertMonths('November-March (Northern) / May-September (Southern)'))
#print(convertMonths('Year-round (Northern and Southern)'))
#!/usr/bin/env python3
#Sam Wiston

from bs4 import BeautifulSoup
import json
import re
import convertTime
import convertMonths
import toInt

allBugs = []

with open("polygon_bug_list.html", "r") as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'html.parser')

    table = soup.findAll('table', {'class':'p-data-table'})
    tableBody = table[0].find('tbody')

    tableLines = tableBody.findAll('tr')

    for bug in tableLines:
        bugObject = {}
        bugData = bug.findAll('td')

        bugObject['id']       = bugData[0].text
        bugObject['name']     = bugData[1].text
        bugObject['location'] = bugData[2].text
        bugObject['price']    = toInt.toInt(bugData[3 ].text)
        bugObject['time']     = convertTime.convertTime(bugData[4].text)
        bugObject['months']   = convertMonths.convertMonths(bugData[5].text)

        allBugs.append(bugObject)

with open("bugs.json", "w") as f:
    bugDump = json.dumps(allBugs)
    f.write(bugDump)
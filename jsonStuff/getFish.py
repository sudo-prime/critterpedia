#!/usr/bin/env python3
#Sam Wiston

from bs4 import BeautifulSoup
import json
import re
import convertTime
import convertMonths
import toInt

allFish = []

with open("polygon_fish_list.html", "r") as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'html.parser')

    table = soup.findAll('table', {'class':'p-data-table'})
    tableBody = table[0].find('tbody')

    tableLines = tableBody.findAll('tr')

    for fish in tableLines:
        fishObject = {}
        fishData = fish.findAll('td')

        fishObject['id']       = fishData[0].text
        fishObject['name']     = fishData[1].text
        fishObject['location'] = fishData[2].text
        fishObject['size']     = fishData[3].text
        fishObject['price']    = toInt.toInt(fishData[4].text)
        fishObject['time']     = convertTime.convertTime(fishData[5].text)
        fishObject['months']   = convertMonths.convertMonths(fishData[6].text)

        allFish.append(fishObject)

with open("fish.json", "w") as f:
    fishDump = json.dumps(allFish)
    f.write(fishDump)
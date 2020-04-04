#!/usr/bin/env python3
#Sam Wiston

from bs4 import BeautifulSoup
import json
import re

with open("bugs_wiki.html", "r") as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'html.parser')

    table = soup.find('div', {'title':'Northern Hemisphere'})
    table = table.find('table', {'class':'sortable'})

    bugs = table.findAll('tr')[1:]
    #tableBody = table[0].find('tbody')

    #tableLines = tableBody.findAll('tr')

    for bug in bugs[0:1]:
        bugData = bug.findAll('td')
        print(bugData[1].find('a')['href'])


    
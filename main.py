#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import re
import time
from settings import URL, applet, key

def get_data(URL):
    resp =  requests.get(URL)
    pat = r"(?<=\[\[\[\"tsp-mr4\",\"tsp-vm\"]).+(?=,\[null,\[\[\"tsp-mr4\")"
    x = re.findall(pat, resp.text)
    x = str(x)
    scores = re.sub(r'\[|\]|null|"|tsp-mr4|tsp-vm|,', ' ', x)
    clean = scores.replace('-       0  ', '\n').replace('             ', ' ')
    clean = clean.replace('\n', '比').replace('    ', '\n')
    return clean.strip()

while True:
    value1 = get_data(URL)
    if len(value1) < 1:
        value1 = '比賽結束!'
        trigger_url = f'https://maker.ifttt.com/trigger/{applet}/with/key/{key}?value1={value1}'
        requests.get(trigger_url)
        break
    else:
        trigger_url = f'https://maker.ifttt.com/trigger/{applet}/with/key/{key}?value1={value1}'
        requests.get(trigger_url)
        time.sleep(15)

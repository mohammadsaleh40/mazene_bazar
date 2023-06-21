import requests
import json

import numpy as np
import pandas as pd
from security import bearer

header = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/114.0",
"Authorization":bearer}


f = open("symbol.csv" , "r")
list_symbole = f.read().split("\n")
dict_symbole = {}
for i in range (len(list_symbole)):
    url = f"https://api-mts.orbis.easytrader.ir/chart/api/datafeed/symbols?symbol={list_symbole[i]}:1"
    r = requests.get(url , headers = header)
    if r.status_code == 200:
        j = json.loads(r.text)
        if j:    
            if j['symbol']:
                dict_symbole[j['symbol']] = list_symbole[i]
with open("list_namad.json", "w") as file:
    json.dump(dict_symbole, file)
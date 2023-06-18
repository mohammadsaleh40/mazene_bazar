import requests
import json
import os
from datetime import datetime

import numpy as np
import pandas as pd
from functions import send_to_bale , search , MarketSheet_to_sarane , send_file_to_bale
bale_chat_id = 5182063095
file = open('list_namad.json' , 'r')
list_symbole = json.load(file)
file.close()
if not os.path.exists("sarane_ha"):
    os.makedirs("sarane_ha")
header = """POST /symbols/api/MarketData/symbol-info-data HTTP/1.1
Host: api-mts.orbis.easytrader.ir
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/114.0
Accept: application/json, text/plain, */*
Accept-Language: fa
Accept-Encoding: gzip, deflate, br
Content-Type: application/json
Content-Length: 23
Referer: https://d.orbis.easytrader.ir/
Origin: https://d.orbis.easytrader.ir
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-site
Authorization: Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImI3MmYyMjczZTE4YTQ0YjQ5OTFmMDg3ODIzNzQyYmI1IiwidHlwIjoiYXQrand0In0.eyJuYmYiOjE2ODcwNDIyNzksImV4cCI6MTY4NzA2Mzg3OSwiaXNzIjoiaHR0cHM6Ly9hY2NvdW50LmVtb2ZpZC5jb20iLCJhdWQiOlsiZWFzeTJfYXBpIiwibXRzX2FwaSIsImh0dHBzOi8vYWNjb3VudC5lbW9maWQuY29tL3Jlc291cmNlcyJdLCJjbGllbnRfaWQiOiJlYXN5X3BrY2UiLCJzdWIiOiJlZDExNzgxZi0yODdkLTQzNWEtODhmZC05NjY1YmNmNzYwMDkiLCJhdXRoX3RpbWUiOjE2ODcwMjgyMjIsImlkcCI6ImxvY2FsIiwicGsiOiJlZDExNzgxZi0yODdkLTQzNWEtODhmZC05NjY1YmNmNzYwMDkiLCJ0d29fZmFjdG9yX2VuYWJsZWQiOiJmYWxzZSIsInByZWZlcnJlZF91c2VybmFtZSI6ImVkMTE3ODFmLTI4N2QtNDM1YS04OGZkLTk2NjViY2Y3NjAwOSIsIm5hbWUiOiJlZDExNzgxZi0yODdkLTQzNWEtODhmZC05NjY1YmNmNzYwMDkiLCJwaG9uZV9udW1iZXIiOiIwOTM2NDg2Njk0MSIsInBob25lX251bWJlcl92ZXJpZmllZCI6dHJ1ZSwiZGlzcGxheV9uYW1lIjoi2YXYrdmF2K8g2LXYp9mE2K0g2LnZhNuMINin2qnYqNix24wiLCJmaXJzdG5hbWUiOiLZhdit2YXYryDYtdin2YTYrSIsImxhc3RuYW1lIjoi2LnZhNuMINin2qnYqNix24wiLCJuYXRpb25hbF9pZCI6IjA5MTAyMDYyNzkiLCJuYXRpb25hbF9pZF92ZXJpZmllZCI6InRydWUiLCJjdXN0b21lcl9pc2luIjoiMTEyOTA5MTAyMDYyNzkiLCJib3Vyc2VfY29kZSI6Iti5INi1INiuNTkyNDEiLCJjcmVhdG9yX2NsaWVudCI6IlJlZ1dlYkFwcCIsImNvbnRyYWN0IjpbIlRlc3RDb250cmFjdF8xLjAiLCJFY29udHJhY3RfMi4wIiwiT21zTW9maWRfMS4wIl0sInNjb3BlIjpbIm9wZW5pZCIsInByb2ZpbGUiLCJlYXN5Ml9hcGkiLCJtdHNfYXBpIiwib2ZmbGluZV9hY2Nlc3MiXSwiYW1yIjpbInB3ZCJdfQ.aiffI_fCtgNIszoixISQ3zqTDZiECEKHkSlIAyjYdW8HFOZf5HmuIYjLbAgGPoNXB8BVY68nz7vkI76j7aGcmKxYeOJpl5bLrjh-xIO0qpaD9N666-o1px-UJUD4uALcDEyKvEflrB4xduGIHrBvdOxXurX8AmB_dXralYEFrbs5jLZHubyDaME2yNJ_AXzzNDsCBic101v5pzsG4Egjwn3T0lmPKsCWjNF62UALEOBHD_5RiAKnnFv-4qq0yXRcfDe579vh5kNahnZkpoFJ063qjPmyQzDV5EOwiDdMn0_Sh6H5zSX9ecgX577XurXMkvL9lOVp_H9z_BnxDY-2_Q
Connection: keep-alive"""

bearer = search(header , "Authorization:" , "\n")
def ersal_sarane(bearer = bearer ,bale_chat_id = bale_chat_id , matn = False , file = True , list_namad = []):
    header = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/114.0",
    "Authorization":bearer}

    url_api = "https://api-mts.orbis.easytrader.ir/ms/api/MarketSheet/all/"

    #f = open("symbol.csv" , "r")
    #list_symbole = f.read().split("\n")
    s = ""
    df_list = []
    now = datetime.now()
    for x in list_namad:
        
        url = url_api+list_symbole[x]
        r = requests.get(url , headers = header)
        if r.status_code == 200:
            sarane_kharid , sarane_foroosh = MarketSheet_to_sarane(r)
            s += x + '\t سرانه خرید:\n'+str(sarane_kharid)+'\n'+'سرانه فروش:\n'+ str(sarane_foroosh)+"\n*-*-*-*-*-*-*-*-\n"
            df_dict = {"code_namad":list_symbole[x] , "namad" : x , "sarane_kharid":sarane_kharid , "sarane_foroosh":sarane_foroosh}
            df_list.append(df_dict)
        else:
            send_to_bale(str(r.status_code) + r.text+"\nهمچین خطایی داده." , bale_chat_id=bale_chat_id)
    if matn:
        send_to_bale(s , bale_chat_id=bale_chat_id)
    df = pd.DataFrame(df_list)
    df["kharid_bar_foroosh"] = df["sarane_kharid"]/df["sarane_foroosh"]
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S.%f")
    df.to_csv("sarane_ha/sarane_"+timestamp+".csv")
    if file:
        send_file_to_bale("sarane_ha/sarane_"+timestamp+".csv", bale_chat_id)

def daryaft_sarane_ha(text):
    list_namad = []
    l = text.split('\n')
    if 'متن:' in text:
        matn = search(text, 'متن:', '\n')
        
        if matn in ['1' , '۱' , 'ok' , 'true' , 'True' , 'TRUE' ,'OK', 'اوکی' , 'باشه']:
            
            matn = True
        else:
            matn = False
        file = search(text, 'فایل:', '\n')
        
        if file in ['0','۰','no','false','False','FALSE','NO','نه','نباشه']:
            
            file = False
        else:
            file = True
    for word in l:
        if word in list_symbole:
            list_namad.append(word)
    #try:
    ersal_sarane(matn = matn , file = file ,list_namad=list_namad)
    #except Exception as e:
    #    send_to_bale(f"درخواست\n{text}\nانجام نشد.\n" +str(e), bale_chat_id= bale_chat_id)
import requests
import json
import os
import time
from datetime import datetime
import pickle
import numpy as np
import pandas as pd
from functions import send_to_bale , search , MarketSheet_to_sarane , send_file_to_bale , convert_to_datetime
bale_chat_id = 5182063095
file = open('list_namad.json' , 'r')
list_symbole = json.load(file)
file.close()
if not os.path.exists("sarane_ha"):
    os.makedirs("sarane_ha")
if not os.path.exists("pickle_ha"):
    os.makedirs("pickle_ha")
header = """GET /ms/api/MarketSheet/all/IRO1GMSH0001 HTTP/1.1
Host: api-mts.orbis.easytrader.ir
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/114.0
Accept: application/json, text/plain, */*
Accept-Language: fa
Accept-Encoding: gzip, deflate, br
Referer: https://d.orbis.easytrader.ir/
Origin: https://d.orbis.easytrader.ir
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-site
Authorization: Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImI3MmYyMjczZTE4YTQ0YjQ5OTFmMDg3ODIzNzQyYmI1IiwidHlwIjoiYXQrand0In0.eyJuYmYiOjE2ODcwNjM4MjIsImV4cCI6MTY4NzA4NTQyMiwiaXNzIjoiaHR0cHM6Ly9hY2NvdW50LmVtb2ZpZC5jb20iLCJhdWQiOlsiZWFzeTJfYXBpIiwibXRzX2FwaSIsImh0dHBzOi8vYWNjb3VudC5lbW9maWQuY29tL3Jlc291cmNlcyJdLCJjbGllbnRfaWQiOiJlYXN5X3BrY2UiLCJzdWIiOiJlZDExNzgxZi0yODdkLTQzNWEtODhmZC05NjY1YmNmNzYwMDkiLCJhdXRoX3RpbWUiOjE2ODcwMjgyMjIsImlkcCI6ImxvY2FsIiwicGsiOiJlZDExNzgxZi0yODdkLTQzNWEtODhmZC05NjY1YmNmNzYwMDkiLCJ0d29fZmFjdG9yX2VuYWJsZWQiOiJmYWxzZSIsInByZWZlcnJlZF91c2VybmFtZSI6ImVkMTE3ODFmLTI4N2QtNDM1YS04OGZkLTk2NjViY2Y3NjAwOSIsIm5hbWUiOiJlZDExNzgxZi0yODdkLTQzNWEtODhmZC05NjY1YmNmNzYwMDkiLCJwaG9uZV9udW1iZXIiOiIwOTM2NDg2Njk0MSIsInBob25lX251bWJlcl92ZXJpZmllZCI6dHJ1ZSwiZGlzcGxheV9uYW1lIjoi2YXYrdmF2K8g2LXYp9mE2K0g2LnZhNuMINin2qnYqNix24wiLCJmaXJzdG5hbWUiOiLZhdit2YXYryDYtdin2YTYrSIsImxhc3RuYW1lIjoi2LnZhNuMINin2qnYqNix24wiLCJuYXRpb25hbF9pZCI6IjA5MTAyMDYyNzkiLCJuYXRpb25hbF9pZF92ZXJpZmllZCI6InRydWUiLCJjdXN0b21lcl9pc2luIjoiMTEyOTA5MTAyMDYyNzkiLCJib3Vyc2VfY29kZSI6Iti5INi1INiuNTkyNDEiLCJjcmVhdG9yX2NsaWVudCI6IlJlZ1dlYkFwcCIsImNvbnRyYWN0IjpbIlRlc3RDb250cmFjdF8xLjAiLCJFY29udHJhY3RfMi4wIiwiT21zTW9maWRfMS4wIl0sInNjb3BlIjpbIm9wZW5pZCIsInByb2ZpbGUiLCJlYXN5Ml9hcGkiLCJtdHNfYXBpIiwib2ZmbGluZV9hY2Nlc3MiXSwiYW1yIjpbInB3ZCJdfQ.p3AKCXlPBwsr9eDQe3j5s93-x4zY4QPD483Qp3VGvCMaR7WHAy84GVUnPSmL6KErYF2mSywEKKYUt0IvdfalW-uOZffCeQ5HrNmWMRKPE5AtDlFn_C80qynbYYzJfZ_ScejZEfxt3lvAUBTh3k_YqoKNoUmdpoDwywBPCCwmZ3QWIek7doeCOcd8BFPnWUITyPbnlGM0hlcvzvv3Smew953EsBFYIC-7Pb5AxjVo_hBhcNVoz8jU9GbTz2YPYDHyDPKjvWa3W1_RkCAne3wSBVAW4IRJT3uXsa69I6WumJUuDKN1SLLgz1LbPY-q-X-AplbNHdPhfZGknaaWMCq7lw
Connection: keep-alive"""

bearer = search(header , "Authorization:" , "\n")
def ersal_sarane(id , bearer = bearer ,bale_chat_id = bale_chat_id , matn = False , file = True , list_namad = [], time = datetime.now()):
    specify_string = str(id)
    my_tuple = (id , bearer , bale_chat_id , matn , file , list_namad , time )
    with open(f'pickle_ha/{specify_string}.pkl', 'wb') as f:
        pickle.dump(my_tuple, f)
    os.system(f"nohup python3 es.py {specify_string} &> output.txt 2>&1 &")
    print(f"nohup python3 es.py {specify_string} &> output.txt 2>&1 &")
def daryaft_sarane_ha(text , id):
    list_namad = []
    l = text.split('\n')
    if 'متن:' in text:
        matn = search(text, 'متن:', '\n')
        
        if matn in ['1' , '۱' , 'ok' , 'true' , 'True' , 'TRUE' ,'OK', 'اوکی' , 'باشه']:
            
            matn = True
        else:
            matn = False
    if "فایل:" in text:
        file = search(text, 'فایل:', '\n')
        
        if file in ['0','۰','no','false','False','FALSE','NO','نه','نباشه']:
            
            file = False
        else:
            file = True
    if "زمان:" in text:
        ti = search(text, "زمان:", '\n')
        try:
            time = convert_to_datetime(ti)
        except Exception as e:
            send_to_bale(f"تبدیل تاریخ زمان و تاریخ موفق نبود.\n {str(e)}" , bale_chat_id=bale_chat_id)
    for word in l:
        if word in list_symbole:
            list_namad.append(word)
    #try:
    ersal_sarane(matn = True , file = True ,list_namad=list_namad, time = time, id = id)
    #except Exception as e:
    #    send_to_bale(f"درخواست\n{text}\nانجام نشد.\n" +str(e), bale_chat_id= bale_chat_id)

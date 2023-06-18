import json
import requests
import pandas as pd
import numpy
import time
from security import bale_token , bale_chat_id
from datetime import datetime, timedelta



def convert_to_datetime(time_str):
    if len(time_str) == 8:  # فرمت hh:mm:ss
        time_str = datetime.now().strftime("%Y-%m-%d ") + time_str
    elif len(time_str) < 19:  # فرمت hh:mm:ss.x
        time_str = datetime.now().strftime("%Y-%m-%d ") + time_str
        
        # تکمیل اعشار به 8 رقم
        decimal_length = len(time_str) - time_str.rindex('.') - 1
        if decimal_length < 6:
            time_str += '0' * (6 - decimal_length)
    
    print(time_str)
    return datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S.%f")

def send_file_to_bale(path , bale_chat_id): 
    with open(path, 'rb') as file:
        url = f'https://tapi.bale.ai/bot{bale_token}/sendDocument'
        files = {'document': file}
        data = {'chat_id': bale_chat_id}
        response = requests.post(url, files=files, data=data)
    return response.text

def MarketSheet_to_sarane(response):
    j = json.loads(response.text)
    if j["buySheets"] != []:
        buy_df = pd.DataFrame(j["buySheets"])
        buy_df["value"] = buy_df["volume"]*buy_df["amount"] 
        #buy_df
        sarane_kharid = buy_df["value"].sum() / buy_df["amount"].sum()
    else:
        sarane_kharid = -1
    if j["sellSheets"] != []:    
        sell_df = pd.DataFrame(j["sellSheets"])
        sell_df["value"] = sell_df["volume"]*sell_df["amount"] 
        #sell_df
        sarane_foroosh = sell_df["value"].sum() / sell_df["amount"].sum()
    else:
        sarane_foroosh = -1
    return sarane_kharid , sarane_foroosh

def add_bearer(bearer):
    f = open("bearer.txt", "a")
    f.write(bearer)
    f.close()

def add_order(order):
    with open('order.txt', 'a') as file:
        file.writelines(order)
def add_time_ersal(time_ersal):
    with open('time_ersal.txt', 'a') as file:
        file.writelines(time_ersal)
def read_bale():
    base_url = "https://tapi.bale.ai/bot"+bale_token+"/getUpdates"
    r = requests.get(base_url)
    return r

def send_to_bale(matn , bale_chat_id = bale_chat_id):
    base_url = "https://tapi.bale.ai/bot"+bale_token+"/sendMessage"


    #id خودم رو توی بله پیدا کردم و اینجا قرار دادم
    parameters = {"chat_id":bale_chat_id , "text": matn}
    r = requests.get(base_url, params=parameters)

def search(s , query , endquery):
    length_s = len(s)
    
    zare = ""
    i = 0
    ebteda = 0
    enteha = length_s
    finded_query = False
    finded_endquery = False
    while i < length_s:

        if s[i] == query[0] and not finded_query:
            finded_query = True

            for j in range(1,len(query)):
                i+=1
                if s[i] != query[j]:
                    finded_query = False
                    break
            if finded_query:
                i+=1
                ebteda = i
        if finded_query and s[i] == endquery[0] and not finded_endquery:
            finded_endquery = True
            enteha = i
            for j in range(1,len(endquery)):
                i+=1
                if s[i] != endquery[j]:
                    finded_endquery = False
                    break
            if finded_endquery:
                
                return s[ebteda:enteha].strip()
        
        i+=1
        #print(s[i])
    return "nabood"
    
def order_orbis(bearer , order):
    pass
    
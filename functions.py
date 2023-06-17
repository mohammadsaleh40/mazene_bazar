import json
import requests
import pandas as pd
import numpy
import time
from security import bale_token , bale_chat_id


def MarketSheet_to_sarane(response):
    j = json.loads(response.text)
    buy_df = pd.DataFrame(j["buySheets"])
    buy_df["value"] = buy_df["volume"]*buy_df["amount"] 
    buy_df
    sarane_kharid = buy_df["value"].sum() / buy_df["amount"].sum()
    sarane_kharid
    sell_df = pd.DataFrame(j["sellSheets"])
    sell_df["value"] = sell_df["volume"]*sell_df["amount"] 
    sell_df
    sarane_foroosh = sell_df["value"].sum() / sell_df["amount"].sum()
    sarane_foroosh
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
    
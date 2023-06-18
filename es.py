import sys
import requests
import json
import os
import time
from datetime import datetime
import pickle
import numpy as np
import pandas as pd
from functions import send_to_bale , search , MarketSheet_to_sarane , send_file_to_bale
bale_chat_id = 5182063095
file = open('list_namad.json' , 'r')
list_symbole = json.load(file)
file.close()

def send_sarane(bearer  ,bale_chat_id , matn , file , list_namad):
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
            kharid_be_milion = set(round(sarane_kharid, -6)/1000000) + ' میلیون'
            foroosh_be_milion = set(round(sarane_foroosh, -6)/1000000) + ' میلیون'
            s += x + '\t سرانه خرید:\n'+kharid_be_milion+'\n'+'سرانه فروش:\n'+ foroosh_be_milion+"\n*-*-*-*-*-*-*-*-\n"
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



if __name__ == "__main__":
    specify_string = sys.argv[1]
    with open(f'pickle_ha/{specify_string}.pkl', 'rb') as file:
        loaded_tuple = pickle.load(file)
    target_time = loaded_tuple[-1]    
    print("wait for target time")
    while True:
        # زمان فعلی
        current_time = datetime.now()

        # مقایسه زمان فعلی با زمان هدف
        if current_time >= target_time:
            break

        time.sleep(0.000005)
        
    send_sarane(*loaded_tuple[1:-1])
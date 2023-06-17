import requests
import json

import numpy as np
import pandas as pd

bearer = "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImI3MmYyMjczZTE4YTQ0YjQ5OTFmMDg3ODIzNzQyYmI1IiwidHlwIjoiYXQrand0In0.eyJuYmYiOjE2ODcwMjgyMjQsImV4cCI6MTY4NzA0OTgyNCwiaXNzIjoiaHR0cHM6Ly9hY2NvdW50LmVtb2ZpZC5jb20iLCJhdWQiOlsiZWFzeTJfYXBpIiwibXRzX2FwaSIsImh0dHBzOi8vYWNjb3VudC5lbW9maWQuY29tL3Jlc291cmNlcyJdLCJjbGllbnRfaWQiOiJlYXN5X3BrY2UiLCJzdWIiOiJlZDExNzgxZi0yODdkLTQzNWEtODhmZC05NjY1YmNmNzYwMDkiLCJhdXRoX3RpbWUiOjE2ODcwMjgyMjIsImlkcCI6ImxvY2FsIiwicGsiOiJlZDExNzgxZi0yODdkLTQzNWEtODhmZC05NjY1YmNmNzYwMDkiLCJ0d29fZmFjdG9yX2VuYWJsZWQiOiJmYWxzZSIsInByZWZlcnJlZF91c2VybmFtZSI6ImVkMTE3ODFmLTI4N2QtNDM1YS04OGZkLTk2NjViY2Y3NjAwOSIsIm5hbWUiOiJlZDExNzgxZi0yODdkLTQzNWEtODhmZC05NjY1YmNmNzYwMDkiLCJwaG9uZV9udW1iZXIiOiIwOTM2NDg2Njk0MSIsInBob25lX251bWJlcl92ZXJpZmllZCI6dHJ1ZSwiZGlzcGxheV9uYW1lIjoi2YXYrdmF2K8g2LXYp9mE2K0g2LnZhNuMINin2qnYqNix24wiLCJmaXJzdG5hbWUiOiLZhdit2YXYryDYtdin2YTYrSIsImxhc3RuYW1lIjoi2LnZhNuMINin2qnYqNix24wiLCJuYXRpb25hbF9pZCI6IjA5MTAyMDYyNzkiLCJuYXRpb25hbF9pZF92ZXJpZmllZCI6InRydWUiLCJjdXN0b21lcl9pc2luIjoiMTEyOTA5MTAyMDYyNzkiLCJib3Vyc2VfY29kZSI6Iti5INi1INiuNTkyNDEiLCJjcmVhdG9yX2NsaWVudCI6IlJlZ1dlYkFwcCIsImNvbnRyYWN0IjpbIlRlc3RDb250cmFjdF8xLjAiLCJFY29udHJhY3RfMi4wIiwiT21zTW9maWRfMS4wIl0sInNjb3BlIjpbIm9wZW5pZCIsInByb2ZpbGUiLCJlYXN5Ml9hcGkiLCJtdHNfYXBpIiwib2ZmbGluZV9hY2Nlc3MiXSwiYW1yIjpbInB3ZCJdfQ.WFeQHkojhduRB7KBa6QLdL9dww0VRDysFDv8R9EDXdDOLZ0hK4b-3uCBmVjilHLO7LljL4lFlKp8-fE2LDAju4pZGOux2hP4sHU76JuQLxjfAI8ZSKaBL0tLQ_oTo2q7EoE8Ryp7rqFADzMKTVsJda0V_7rmpUdYbIcn6yzs4s7wmSGna36hSuGxjQIr6R1ey-hd8FXS-dr_riLHV_SiFgRYCFH58QmJd-WlX3MbXztYeI_sTjiHkVj4LX7W05G6F7UKYc3dhFv088fXjwkf6gZnUh_Kf9Bsr5AXdR_YJuCFLHEXg2NypUFwc90ZgevBQP7EUJEYxYAIznAkdMildg"

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
        
        if j['symbol']:

            dict_symbole[list_symbole[i]] = j['symbol']
with open("list_namad.json", "w") as file:
    json.dump(dict_symbole, file)
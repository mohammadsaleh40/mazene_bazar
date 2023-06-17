import requests
from security import bearer
session = requests.Session()
url = "https://api-mts.orbis.easytrader.ir/ms/api/MarketSheet/all/IRO1BMLT0001"
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/114.0",
#"Accept": "application/json, text/plain, */*",
#"Accept-Language": "fa",
#"Accept-Encoding": "gzip, deflate, br",
#"Referer": "https://d.orbis.easytrader.ir/",
#"Origin": "https://d.orbis.easytrader.ir",
#"Sec-Fetch-Dest": "empty",
#"Sec-Fetch-Mode": "cors",
#"Sec-Fetch-Site": "same-site",
"Authorization":bearer,
#"Connection": "keep-alive",
}
response = session.get(url , headers = headers)
print(response.text)
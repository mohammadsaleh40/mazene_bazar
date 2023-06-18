import requests
from security import bale_token
from daryaft_mazene import daryaft_sarane_ha
bale_chat_id = 5182063095

def main():
    
   
   
    # شنیدن پاسخ کاربر با استفاده از Long Polling
    offset = 0  # آفست پیام‌ها
    while True:
        # آدرس API تلگرام برای دریافت بروزرسانی‌ها
        get_updates_url = f'https://tapi.bale.ai/bot{bale_token}/getUpdates?offset={offset}'

        # درخواست GET برای دریافت بروزرسانی‌ها
        response = requests.get(get_updates_url)

        # بررسی کد وضعیت پاسخ
        if response.status_code == 200:
            data = response.json()
            if 'result' in data and len(data['result']) > 0:
                for result in data['result']:
                    if 'message' in result and 'text' in result['message']:
                        text = result['message']['text']
                        chat_id = result['message']['chat']['id']
                        # بررسی درخواست کاربر
                        if '/sarane' in text and chat_id == bale_chat_id:
                            daryaft_sarane_ha(text)
                    offset = result['update_id'] + 1
        else:
            # پردازش خطا
            print(f'Error: {response.status_code}')

if __name__ == '__main__':
    main()
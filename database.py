# %%
import sqlite3
# %%
# برقراری ارتباط با پایگاه داده SQLite
conn = sqlite3.connect('mazene.db')

# %%
cursor = conn.cursor()
# %%
import pandas as pd
import json
with open ('list_namad.json','r') as f:
    j = json.load(f)


j
# %%
j.keys()
j.values()
# %%
list(j.keys())
# %%
[[list(j.keys())],[list(j.values())]]
# %%
df = pd.DataFrame([j.values(),j.keys()] , index=['code' , 'namad'])
df = df.T
df
# %%

# %%
for i in range(5):
    a = df.loc[i]
    print(list(a))


# %%
# ایجاد جدول
#cursor.execute('''CREATE TABLE symbols (namad TEXT, code TEXT)''')

# %%
for i in range(len(df)):
    a = df.loc[i]
    cursor.execute('''INSERT INTO symbols (namad , code) VALUES (? , ?)''' , a)


# ثبت تغییرات و بستن اتصال
conn.commit()
conn.close()
# %%

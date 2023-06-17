import pandas as pd
d = open("h2" , "r")
ll = []
l = d.read().split("string(12)")
print(len(l))

for i in l:
    x = i[2:14]
    if x[:2] == 'IR':
        
        ll.append(x)
df = pd.DataFrame(ll)
print(df.head())
df.to_csv("symbol.csv" , index= False ,header=False)
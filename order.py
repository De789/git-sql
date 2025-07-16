import numpy as np 
import pandas as pd

df=pd.read_csv(r"D:\orders.csv")
# print(df.head(5))
# print(df.columns)
# print(df['Ship Mode'])

df.columns=df.columns.str.lower()
# print(df)
df.columns=df.columns.str.replace(" ","_")
# print(df.columns)
# print(df.head(5))
df['discount']=df['list_price']*0.01
df['sale_price']=df['list_price']-df['discount']
df['profit']=df['list_price']-df['sale_price']
df.drop(columns=['list_price','discount'],inplace=True)
# df['order_date'] = pd.to_datetime(df['order_date'], format="%y-%m-%d")
# print(df.head(5))
# print(df.dtypes)
# print(df.columns)

print(df.to_csv('orders.csv', index=False))
 
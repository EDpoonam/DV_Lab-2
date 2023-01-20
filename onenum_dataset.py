# -*- coding: utf-8 -*-
"""OneNum dataset

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IbqaApFd08sFZwylJtlRboVG3iABhYNj

AIRBNB PRICES ON THE FRENCH RIVIERA
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("https://raw.githubusercontent.com/holtzy/data_to_viz/master/Example_dataset/1_OneNum.csv")
df['price'].describe()

df['price']=df['price'][(df['price']<300)]
df['price'].describe()

# check out missing data
total = df.isnull().sum().sort_values(ascending=False)
percent = (df.isnull().sum()/df.isnull().count()).sort_values(ascending=False)
missing_df = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
missing_df.head(20)

# Select only numeric data and impute missing values as 0
numerics = ['uint8','int16', 'int32', 'int64', 'float16', 'float32', 'float64']
data = df \
    .select_dtypes(include=numerics) \
    .fillna(0) \
    .values

a=df["price"]<300
a.head()

d=sns.displot(df["price"],fill="#69b3a2", color="#e9ecef", alpha=0.9)
d.set(title='Night price distribution of Airbnb appartements')
plt.show()
## bin size =10
d1=sns.displot(df["price"],bins=10,fill="#69b3a2", color="#e9ecef", alpha=0.9)
d1.set(title='Night price distribution of Airbnb appartements')
plt.show()
## bin size =2
d2=sns.displot(df["price"],bins=2,fill="#69b3a2", color="#e9ecef", alpha=0.9)
d2.set(title='Night price distribution of Airbnb appartements')
plt.show()

d2=sns.kdeplot(data=df,x=df["price"],fill="#69b3a2", color="#e9ecef", alpha=0.7,bw=10)
d2.set(title='Band Width 10')
plt.show()
d3=sns.kdeplot(data=df,x=df["price"],fill="#69b3a2", color="#e9ecef", alpha=0.7,bw=2)
d3.set(title='Band Width 2')
plt.show()


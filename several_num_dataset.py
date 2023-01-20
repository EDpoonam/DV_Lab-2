# -*- coding: utf-8 -*-
"""Several_Num Dataset

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CkjvD5y5AxNT8ZdACQ7WnOIlrke_rJEp
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("https://raw.githubusercontent.com/holtzy/data_to_viz/master/Example_dataset/6_SeveralNum.csv")
df.head()

# Check distribution using histogram
df[['disp','drat','hp','mpg','wt','qsec']].hist(figsize=(10,8))
plt.tight_layout()
plt.show()

d1=sns.histplot(df['disp'],fill="#69b3a2", color="#e9ecef",alpha=.9,bins=50)
d1.set(title='disp')
plt.show()


d2=sns.histplot(df['drat'],fill="#69b3a2", color="#e9ecef",alpha=.9,bins=50)
d2.set(title='drat')
plt.show()


d3=sns.histplot(df['hp'],fill="#69b3a2", color="#e9ecef",alpha=.9,bins=50)
d3.set(title='hp')
plt.show()


d4=sns.histplot(df['mpg'],fill="#69b3a2", color="#e9ecef",alpha=.9,bins=50)
d4.set(title='mpg')
plt.show()


d5=sns.histplot(df['qsec'],fill="#69b3a2", color="#e9ecef",alpha=.9,bins=50)
d5.set(title='qsec')
plt.show()


d6=sns.histplot(df['wt'],fill="#69b3a2", color="#e9ecef",alpha=.9,bins=50)
d6.set(title='wt')
plt.show()

# Correlogram
g = sns.pairplot(df[['disp','drat','hp','mpg','wt','qsec']], diag_kind="hist")

# Dendrogram
sns.clustermap(df,figsize=(7, 5),row_cluster=False, dendrogram_ratio=(.1, .2),cbar_pos=(0, .2, .03, .4))

# Heatmap
corr = df[['disp','drat','hp','mpg','wt','qsec']].corr()
plt.figure(figsize=(20,9))
a = sns.heatmap(corr, annot=True, fmt='.2f')
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

train=pd.read_csv(r'train.csv')
df=train.copy()

print(df.shape)
print(df.columns)
print(df.index)
print(df['Pclass'].value_counts())

print(df.describe())

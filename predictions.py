
from re import S
import pandas as pd
import numpy as np


df = pd.read_csv("Titanic.csv")
#print(df.head())

print(df.dtypes)


age = df['Age']
survived = df["Survived"]

list_of_indexes_of_records_that_need_to_be_removed = []
age_after_purge = []
survived_after_purge = []

for i in range(len(age)):
  try:
    c = int(age[i])
    d = int(survived[i])
    age_after_purge.append(c)
    survived_after_purge.append(d)
  except:
    pass



import tensorflow as tf
from tensorflow import keras


model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='adam',loss='mean_squared_error')

"""xs = np.array([15,50,30,50,60,70],dtype=float)
ys = np.array([1,0,1,0,0,0],dtype=float)"""

xs = list(age_after_purge)
ys = list(survived_after_purge)

model.fit(xs, ys, epochs=150)

result =  model.predict([50,30])
print(result)
import pandas as pd
import numpy as np


df = pd.read_csv("Titanic.csv")
#print(df.head())

print(df.dtypes)


age = df['Sex']
survived = df["Survived"]

age_after_purge = []
survived_after_purge = []


print(len(age))
for i in range(len(age)):

  try:
    c = str(age[i])
    d = int(survived[i])


    if c == "female":
        c = 0
    else: 
        c = 1

    age_after_purge.append(c)
    survived_after_purge.append(d)
  except:
    pass

print("yop")

import tensorflow as tf
from tensorflow import keras


model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='adam',loss='mean_squared_error')

"""xs = np.array([15,50,30,50,60,70],dtype=float)
ys = np.array([1,0,1,0,0,0],dtype=float)"""

xs = list(age_after_purge)
ys = list(survived_after_purge)

model.fit(xs, ys, epochs=200)

result =  model.predict([0,1])
print(result)
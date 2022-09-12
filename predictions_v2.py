import pandas as pd
import numpy as np


df = pd.read_csv("Titanic.csv")
#print(df.head())

print(df.dtypes)


age = df['Age']
survived = df["Survived"]
gender = df["Sex"]


list_of_indexes_of_records_that_need_to_be_removed = []
age_after_purge = []
survived_after_purge = []
gender_after_purge = []

"""for i in range(len(age)):
	try:
    	c = int(age[i])
    	d = int(survived[i])
		e = str(gender[i])

    	age_after_purge.append(c)
    	survived_after_purge.append(d)
	except:
		pass

"""

for i in range(len(age)):
	try:
		c = int(age[i])
		d = int(survived[i])
		e = str(gender[i])

		age_after_purge.append(c)
		survived_after_purge.append(d)
		
		if e == "female":
			gender_after_purge.append(0)
		elif e == "male":
			gender_after_purge.append(1)
		else:
			print(e)

	except:
		pass

import tensorflow as tf
from tensorflow import keras


model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='adam',loss='mean_squared_error')


xs = list(age_after_purge)
ys = list(survived_after_purge)
zs = list(gender_after_purge)

model.fit(xs, ys, epochs=250)
based_on_age =  model.predict([30,90])


model.fit(zs, ys, epochs=250)
based_on_gender = model.predict([0,1])

print(f"age {based_on_age} gender {based_on_gender}")


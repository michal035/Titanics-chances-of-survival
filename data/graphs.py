from cProfile import label
import numpy as np
import matplotlib.pyplot as plt
import main

# Collecting all the data from main file -> both the number of passengers and survivors

male = main.data1.number_of_survivors_that_were_male
female = main.data1.number_of_survivors_that_were_female
Pmale = main.data1.number_of_passengers_that_were_male
Pfemale = main.data1.number_of_passengers_that_were_female

FirstClass = main.data1.number_of_survivors_in_1stclass
SecondClass = main.data1.number_of_survivors_in_2ndclass
ThirdClass = main.data1.number_of_survivors_in_3rdclass
PFirstClass = main.data1.number_of_passengers_in_1stclass
PSecondClass = main.data1.number_of_passengers_in_2ndclass
PThirdClass = main.data1.number_of_passengers_in_3rdclass

below18 = main.data1.number_of_survivors_that_were_below_age18
below60 = main.data1.number_of_survivors_that_were_below_age60
above60 = main.data1.number_of_survivors_above_age_of_60
Pbelow18 = main.data1.number_of_passengers_that_were_below_age18
Pbelow60 = main.data1.number_of_passengers_that_were_below_age60
Pabove60 = main.data1.number_of_passengers_above_age_of_60

# Counting the percentage of people which survived

m = (male/Pmale)*100
f = (female/Pfemale)*100

st = (FirstClass/PFirstClass)*100
nd = (SecondClass/PSecondClass)*100
rd = (ThirdClass/PThirdClass)*100

b18 = (below18/Pbelow18)*100
b60 = (below60/Pbelow60)*100
a60 = (above60/Pabove60)*100

#Setting up parameters for subplots

Pleft = [1, 2]
Ptable = ["male", "female"]
Pheight = [m, f]

left = [1, 2, 3]
height = [st, nd, rd]
tick_label = ['1stClass', '2ndClass', '3rdClass']

left2 = [1, 2, 3]
heightt = [b18, b60, a60]
trick_labell = ['<18', '<60', '>60']

activities = ['female', 'male']
slices = [female, male]
colors = ['#ff6666', '#00bfff']

plt.rcdefaults()

# Initialization of plot with subplots

fig, ax = plt.subplots(2, 2)

# First subplot

ax[0, 0].pie(slices, labels=activities, colors=colors,
             startangle=90, shadow=True, explode=(0.02, 0.02),
             radius=1.2, autopct='%1.1f%%', wedgeprops={'linewidth': 1.5, 'edgecolor': "#330000", 'alpha': 0.5})
ax[0, 0].set_title('Percentage of survivors based on their gender')

# Second subplot

ax[0, 1].set_xlabel('Class')
ax[0, 1].set_ylabel('Number of survivors')
ax[0, 1].set_title('Chances of survival based on class')
ax[0, 1].bar(left2, height, tick_label=tick_label,
             width=1, color=['#99e6ff', '#0086b3', '#66d9ff'], edgecolor="#330000")
ax[0, 1].spines.top.set_visible(False)
ax[0, 1].spines.right.set_visible(False)

# Third subplot

ax[1, 1].bar(left2, heightt, tick_label=trick_labell,
             width=0.8, color=['#33ff99', '#57db99', '#70c299'], edgecolor="#330000", linewidth=1.5, alpha = 0.8)
ax[1, 1].set_xlabel('Age')
ax[1, 1].set_ylabel('Chances of survival')
ax[1, 1].set_title('Chances of survival based on age')
ax[1, 1].spines.top.set_visible(False)
ax[1, 1].spines.right.set_visible(False)

# Fourth subplot

ax[1, 0].set_title('Chances of survival based on gender')
ax[1, 0].bar(Pleft, Pheight, tick_label=Ptable,
             width=0.8, color=['#4d79ff', '#ff4d4d'], edgecolor="#330000", linewidth=1.5, alpha = 0.85)
ax[1, 0].set_xlabel('Sex')
ax[1, 0].set_ylabel('Chances of survival')
ax[1, 0].spines.top.set_visible(False)
ax[1, 0].spines.right.set_visible(False)

plt.subplots_adjust(left=0.1,
                    bottom=0.1,
                    right=0.9,
                    top=0.9,
                    wspace=0.9,
                    hspace=0.9)

# fig.tight_layout() -> you might need to uncomment this if it displays in odd way

#saving whole plot to .png file

fig.set_size_inches(8.5, 6)
fig.savefig('Graph', dpi=100)

fig.canvas.manager.set_window_title(
    'Data analysis and prediction of survivors on the titanic dataset')

plt.show()

from cProfile import label
import matplotlib.pyplot as plt
import main

all = 1313

male = main.data1.number_of_surviors_that_were_male
female = main.data1.number_of_surviors_that_were_female
Pmale = main.data1.number_of_passengers_that_were_male
Pfemale = main.data1.number_of_passengers_that_were_female

FirstClass = main.data1.number_of_surviors_in_1stclass
SecondClass = main.data1.number_of_surviors_in_2ndclass
ThirdClass = main.data1.number_of_surviors_in_3rdclass
PFirstClass = main.data1.number_of_passengers_in_1stclass
PSecondClass = main.data1.number_of_passengers_in_2ndclass
PThirdClass = main.data1.number_of_passengers_in_3rdclass

below18 = main.data1.number_of_survivors_that_were_below_age18
below60 = main.data1.number_of_survivors_that_were_below_age60
above60 = main.data1.number_of_surviors_above_age_of_60
Pbelow18 = main.data1.number_of_passengers_that_were_below_age18
Pbelow60 = main.data1.number_of_passengers_that_were_below_age60
Pabove60 = main.data1.number_of_passengers_above_age_of_60


# Implemnt this in some time -> fig.savefig('out.png', dpi=100)

# Test graph
"""
fig1 = plt.figure(1)
x = [1,2,3]
y = [2,4,5]

plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.plot(x, y, label="pierwsza")

x1 = [1,2,3]
y1 = [2,3,2]

plt.plot(x1,y1, label="druga")
plt.xlabel('x - axis')
plt.ylabel('y - axis')
"""


m = (male/Pmale)*100
f = (female/Pfemale)*100

st = (FirstClass/PFirstClass)*100
nd = (SecondClass/PSecondClass)*100
rd = (ThirdClass/PThirdClass)*100

b18 = (below18/Pbelow18)*100
b60 = (below60/Pbelow60)*100
a60 = (above60/Pabove60)*100


print(above60)
print(Pabove60)

Pleft = [1, 2]
Ptable = ["male", "female"]
Pheight = [m, f]

left = [1, 2, 3]
height = [st, nd, rd]
tick_label = ['1stClass', '2ndClass', '3rdClass']

left2 = [1, 2, 3]
heightt = [b18, b60, a60]
trick_labell = ['<18', '<60', '>60']

"""
plt.bar(left, height, tick_label=tick_label,
        width=0.8, color=['#99e6ff', '#0086b3', '#66d9ff'])


plt.xlabel('Class')

plt.ylabel('Number of Surviors')
plt.title('Number of Surviors based on passenger class')
"""

#fig2 = plt.figure(2)

activities = ['female', 'male']
slices = [female, male]
colors = ['#ff6666', '#00bfff']

"""
plt.title("Chances of survival")
plt.pie(slices, labels=activities, colors=colors,
        startangle=90, shadow=True, explode=(0.02, 0.02),
        radius=1.2, autopct='%1.1f%%')
"""


plt.rcdefaults()
# plt.legend()

fig, ax = plt.subplots(2, 2)

ax[0, 0].pie(slices, labels=activities, colors=colors,
             startangle=90, shadow=True, explode=(0.02, 0.02),
             radius=1.2, autopct='%1.1f%%')
ax[0, 0].set_title('Percentage of surviors based on their gender')


ax[0, 1].set_xlabel('Class')
ax[0, 1].set_ylabel('Number of Surviors')
ax[0, 1].set_title('Chances of survival based on class')
ax[0, 1].legend(['First class', 'Second class', 'Third class'])
ax[0, 1].bar(left2, height, tick_label=tick_label,
             width=0.8, color=['#99e6ff', '#0086b3', '#66d9ff'])


ax[1, 1].bar(left2, heightt, tick_label=trick_labell,
             width=0.8, color=['#cc5200', '#ff751a', '#ffb380'])
ax[1, 1].set_xlabel('Age')
ax[1, 1].set_ylabel('Number of Surviors')
ax[1, 1].set_title('Chances of survival based on age of the pasanger')

ax[1, 0].set_title('Chances of survival based on gender')
ax[1, 0].bar(Pleft, Pheight, tick_label=Ptable,
             width=0.8, color=['#668f3d', '#cc3300'])
ax[1, 0].set_xlabel('Sex')
ax[1, 0].set_ylabel('Chances of survival')


plt.subplots_adjust(left=0.1,
                    bottom=0.1,
                    right=0.9,
                    top=0.9,
                    wspace=0.9,
                    hspace=0.9)
# fig.tight_layout()
fig.set_size_inches(8.5, 6)
fig.savefig('testpng', dpi=100)

fig.canvas.manager.set_window_title('Data analysis and prediction of survivors on the titanic dataset')
plt.show()


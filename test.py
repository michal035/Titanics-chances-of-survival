from cProfile import label
import matplotlib.pyplot as plt
import a

all = 1313
male = a.data1.number_of_surviors_that_were_male
female = a.data1.number_of_surviors_that_were_female
FirstClass = a.data1.number_of_surviors_in_1stclass
SecondClass = a.data1.number_of_surviors_in_2ndclass
ThirdClass = a.data1.number_of_surviors_in_3rdclass

#Implemnt this in some time -> fig.savefig('out.png', dpi=100)

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

#fig3 = plt.figure(3)

left = [1, 2, 3]
height = [FirstClass, SecondClass, ThirdClass]
tick_label = ['1stClass', '2ndClass', '3rdClass']

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


# plt.legend()

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.pie(slices, labels=activities, colors=colors,
        startangle=90, shadow=True, explode=(0.02, 0.02),
        radius=1.2, autopct='%1.1f%%')
ax1.set_title('Chances of survival, based on sex')
ax2.bar(left, height, tick_label=tick_label,
        width=0.8, color=['#99e6ff', '#0086b3', '#66d9ff'])
ax2.set_xlabel('Class')
ax2.set_ylabel('Number of Surviors')
ax2.set_title('Number of Surviors based on passenger class')
ax2.legend(['First class','Second class', 'Third class'])



plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.9, 
                    hspace=0.9)

#fig.tight_layout()
fig.set_size_inches(8.5,6)
fig.savefig('testpng', dpi=100)
plt.show()

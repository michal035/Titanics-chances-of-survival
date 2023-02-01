import pandas as pd
import time



# THIS IS MY OLD CODE IT BADLY NEEDS A REMAKE IT'S NOT THAT IMPORTANT 
# It just counts how many people from each category  survived - how many woman that are aged <60 etc.


class a:
    def __init__(self, Name="None", PClass="None", Age="None", Sex="None", Survived=0):
        self.Name = Name
        self.PClass = PClass
        self.Age = Age
        self.Sex = Sex
        self.Survived = Survived


#This is better faster way to count people, it's checking data from our class not from .csv file
# Count certain parameter - Age 19 but it can return either everyone or only passengers that survived, in order to count survivers last parameter needs to be 0
# I don't think i resolved this in the bets possible way, but i wanted it to be kind of universal, that's why it looks how it looks

    def count_ppl_the_other_way(self, key, key_value, Survived=3):
        match key:
            case 'PClass':
                if self.PClass == key_value and self.Survived != Survived:
                    return 1
                else:
                    return 0
            case 'Age':
                if self.Age == key_value and self.Survived != Survived:
                    return 1
                else:
                    return 0
            case 'Sex':
                if self.Sex == key_value and self.Survived != Survived:
                    return 1
                else:
                    return 0
            case 'Survived':
                if self.Survived == key_value and self.Survived != Survived:
                    return 1
                else:
                    return 0

#This funcion is just to count people in certain age range - key_value1 to key_value2

    def count_ppl_the_other_way_with_paratr(self, key, key_value, key_value1, key_value2, Survived=3):
        if key == "Age" and self.Survived != Survived:
            if self.Age >= key_value1 and self.Age < key_value2:
                return 1
            else:
                return 0
        else:
            return 0

#Here is class just to store each 'variable'

class data:
    def __init__(self):
        self.number_of_survivors = 0
        self.number_of_survivors_that_were_below_age18 = 0
        self.number_of_survivors_that_were_below_age60 = 0
        self.number_of_survivors_above_age_of_60 = 0
        self.number_of_survivors_that_were_male = 0
        self.number_of_survivors_that_were_female = 0
        self.number_of_survivors_in_1stclass = 0
        self.number_of_survivors_in_2ndclass = 0
        self.number_of_survivors_in_3rdclass = 0

        self.number_of_passengers = 0
        self.number_of_passengers_that_were_below_age18 = 0
        self.number_of_passengers_that_were_below_age60 = 0
        self.number_of_passengers_above_age_of_60 = 0
        self.number_of_passengers_that_were_male = 0
        self.number_of_passengers_that_were_female = 0
        self.number_of_passengers_in_1stclass = 0
        self.number_of_passengers_in_2ndclass = 0
        self.number_of_passengers_in_3rdclass = 0

#Self explanatory

    def adding_data(self, key, value):
        match key:
            case 'number_of_survivors':
                self.number_of_survivors = value
            case 'number_of_survivors_that_were_below_age18':
                self.number_of_survivors_that_were_below_age18 = value
            case 'number_of_survivors_that_were_below_age60':
                self.number_of_survivors_that_were_below_age60 = value
            case 'number_of_survivors_above_age_of_60':
                self.number_of_survivors_above_age_of_60 = value
            case 'number_of_survivors_that_were_male':
                self.number_of_survivors_that_were_male = value
            case 'number_of_survivors_that_were_female':
                self.number_of_survivors_that_were_female = value
            case 'number_of_survivors_in_1stclass':
                self.number_of_survivors_in_1stclass = value
            case 'number_of_survivors_in_2ndclass':
                self.number_of_survivors_in_2ndclass = value
            case 'number_of_survivors_in_3rdclass':
                self.number_of_survivors_in_3rdclass = value


pd.options.display.max_rows = 10

df = pd.read_csv('Titanic.csv') # You can use different file, as long as all of the columns and data types in are in the same order

# Here is created object for each row in .csv file

objs = [a(df.iloc[_, 0], df.iloc[_, 1], df.iloc[_, 2],
          df.iloc[_, 3], df.iloc[_, 4]) for _ in range(len(df))]

test = a()

# Most basic way to count people-  slow, bad, getting data from .csv

def counting_stuff(key, key_value):

    return test.count_ppl(key, key_value)

    """
    print(test.count_ppl("PClass", "1st"))
    print(test.count_ppl("Age", 25))  
    """

# Better faster, better way to count people, with survived paramter - on deafult it will count all the passengers

def counting_ppl_the_other_way(df, key, key_value, survived=3):  
    amm = 0
    for _ in range(len(df)):
        amm = amm + objs[_].count_ppl_the_other_way(key, key_value, survived)
    return amm

# example use case -> last agrgument is optional - pass 0 in order to count only survivors
#print(counting_ppl_the_other_way(df, "PClass", "1st", 0))

# Same function, just to count people of certain age (18-60 etc.)

def count_ppl_the_other_way_with_paratr(key, key_value, key_value1, key_value2, survived=3):
    amm = 0
    for _ in range(len(df)):
        amm = amm + objs[_].count_ppl_the_other_way_with_paratr(
            key, key_value, key_value1, key_value2, survived)
    return amm

#Here is function so u can check the speed of each functions yourself 

def speed_test(df):
    s = time.time()
    print(counting_ppl_the_other_way(df, "PClass", "1st"))
    print(time.time() - s)

    s = time.time()
    print(counting_stuff("PClass", "1st"))
    print(time.time() - s)

# speed_test(df)

# through -> don't pay attanetion to this 

data1 = data()

#Here we is function fill our data class with actual data

def filling_number_of_survivors(df, data1, key, dff, keyy, keyy_value, survived=3):
    data1.adding_data(key, counting_ppl_the_other_way(
        dff, keyy, keyy_value, survived))

#Here is function to add data with age range

def filling_number_of_survivors_with_paratr(df, data1, key, keyy, key_value, key_value1, key_value2, survived=3):
    data1.adding_data(key, count_ppl_the_other_way_with_paratr(
        keyy, key_value, key_value1, key_value2, survived))  

#Here we collect we pass data about passengers not survivors 

def filling_number_of_passengers(df):
        data1.number_of_passengers = len(df)
        data1.number_of_passengers_in_1stclass = counting_ppl_the_other_way(df,"PClass","1st")
        data1.number_of_passengers_in_2ndclass = counting_ppl_the_other_way(df,"PClass", "2nd")
        data1.number_of_passengers_in_3rdclass = counting_ppl_the_other_way(df,"PClass", "3rd")
        data1.number_of_passengers_that_were_male = counting_ppl_the_other_way(df,"Sex","male")
        data1.number_of_passengers_that_were_female = counting_ppl_the_other_way(df,"Sex","female")

        data1.number_of_passengers_that_were_below_age18 = count_ppl_the_other_way_with_paratr("Age","NaN",0,18)
        data1.number_of_passengers_that_were_below_age60 = count_ppl_the_other_way_with_paratr("Age","NaN",0,60)
        data1.number_of_passengers_above_age_of_60 = count_ppl_the_other_way_with_paratr("Age","NaN",60,200)
        
#Here we actually add data of survivors

def collecting_all_data():
    filling_number_of_survivors(
        df, data1, 'number_of_survivors', df, 'Survived', 1, 3)
    filling_number_of_survivors(
        df, data1, 'number_of_survivors_that_were_male', df, 'Sex', 'male', 0)
    filling_number_of_survivors(
        df, data1, 'number_of_survivors_that_were_female', df, 'Sex', 'female', 0)
    filling_number_of_survivors(
        df, data1, 'number_of_survivors_in_1stclass', df, 'PClass', '1st', 0)
    filling_number_of_survivors(
        df, data1, 'number_of_survivors_in_2ndclass', df, 'PClass', '2nd', 0)
    filling_number_of_survivors(
        df, data1, 'number_of_survivors_in_3rdclass', df, 'PClass', '3rd', 0)
    filling_number_of_survivors_with_paratr(
        df, data1, 'number_of_survivors_that_were_below_age18', 'Age', 'NaN', 0, 18, 0)
    filling_number_of_survivors_with_paratr(
        df, data1, 'number_of_survivors_that_were_below_age60', 'Age', 'NaN', 0, 60, 0)
    filling_number_of_survivors_with_paratr(
        df, data1, 'number_of_survivors_above_age_of_60', 'Age', 'NaN', 60, 200, 0)


collecting_all_data()
filling_number_of_passengers(df)

#Here are some tests ->  play around

print(data1.number_of_survivors)
print(data1.number_of_passengers)
print(data1.number_of_survivors_that_were_male)
print(data1.number_of_survivors_in_1stclass)
print(counting_ppl_the_other_way(df, 'PClass', '1st', 0))
print(data1.number_of_survivors_above_age_of_60)

print(data1.number_of_passengers_that_were_below_age18)
print(data1.number_of_survivors_that_were_below_age18)



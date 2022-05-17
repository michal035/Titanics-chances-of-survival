import pandas as pd
import time


class a:
    def __init__(self, Name="None", PClass="None", Age="None", Sex="None", Survived=0):
        self.Name = Name
        self.PClass = PClass
        self.Age = Age
        self.Sex = Sex
        self.Survived = Survived

    def count_ppl(self, key, key_value):
        amount_of_ppl = 0
        list_of_stuff = ["Name", "PClass", "Age",
                         "Sex", "Survived"], [0, 1, 2, 3, 4]
        key = list_of_stuff[0].index(key)
        key = list_of_stuff[1][key]
        for _ in range(len(df)):
            if df.iloc[_][key] == key_value:  # here
                amount_of_ppl = amount_of_ppl + 1
        return amount_of_ppl

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

    def count_ppl_the_other_way_with_paratr(self, key, key_value, key_value1, key_value2, Survived=3):
        if key == "Age" and self.Survived != Survived:
            if self.Age >= key_value1 and self.Age < key_value2:
                return 1
            else:
                return 0
        else:
            return 0


class data:
    def __init__(self):
        self.number_of_survivors = 0
        self.number_of_survivors_that_were_below_age18 = 0
        self.number_of_survivors_that_were_below_age60 = 0
        self.number_of_surviors_between_age18and60 = 0
        self.number_of_surviors_that_were_male = 0
        self.number_of_surviors_that_were_female = 0
        self.number_of_surviors_in_1stclass = 0
        self.number_of_surviors_in_2ndclass = 0
        self.number_of_surviors_in_3rdclass = 0

        self.number_of_passengers = 0
        self.number_of_passengers_that_were_below_age18 = 0
        self.number_of_passengers_that_were_below_age60 = 0
        self.number_of_passengers_between_age18and60 = 0
        self.number_of_passengers_that_were_male = 0
        self.number_of_passengers_that_were_female = 0
        self.number_of_passengers_in_1stclass = 0
        self.number_of_passengers_in_2ndclass = 0
        self.number_of_passengers_in_3rdclass = 0

    def adding_data(self, key, value):
        match key:
            case 'number_of_survivors':
                self.number_of_survivors = value
            case 'number_of_survivors_that_were_below_age18':
                self.number_of_survivors_that_were_below_age18 = value
            case 'number_of_survivors_that_were_below_age60':
                self.number_of_survivors_that_were_below_age60 = value
            case 'number_of_surviors_between_age18and60':
                self.number_of_surviors_between_age18and60 = value
            case 'number_of_surviors_that_were_male':
                self.number_of_surviors_that_were_male = value
            case 'number_of_surviors_that_were_female':
                self.number_of_surviors_that_were_female = value
            case 'number_of_surviors_in_1stclass':
                self.number_of_surviors_in_1stclass = value
            case 'number_of_surviors_in_2ndclass':
                self.number_of_surviors_in_2ndclass = value
            case 'number_of_surviors_in_3rdclass':
                self.number_of_surviors_in_3rdclass = value


pd.options.display.max_rows = 10

df = pd.read_csv('Titanic.csv')


# objs = [a() for _ in range(len(df))]

objs = [a(df.iloc[_, 0], df.iloc[_, 1], df.iloc[_, 2],
          df.iloc[_, 3], df.iloc[_, 4]) for _ in range(len(df))]

test = a()

"""
for _ in range(10):
    print(objs[_].name, objs[_].Pclass, objs[_].age,
          objs[_].psex, objs[_].Survived)
"""


def counting_stuff(key, key_value):

    return test.count_ppl(key, key_value)

    """
    print(test.count_ppl("PClass", "1st"))
    print(test.count_ppl("Age", 25))  # wiek i czy survived int
    """

# szybsze


def counting_ppl_the_other_way(df, key, key_value, survived=3):  # szybsze
    amm = 0
    for _ in range(len(df)):
        amm = amm + objs[_].count_ppl_the_other_way(key, key_value, survived)
    return amm


def count_ppl_the_other_way_with_paratr(key, key_value, key_value1, key_value2, survived=3):
    amm = 0
    for _ in range(len(df)):
        amm = amm + objs[_].count_ppl_the_other_way_with_paratr(
            key, key_value, key_value1, key_value2, survived)
    return amm


def speed_test(df):
    s = time.time()
    print(counting_ppl_the_other_way(df, "PClass", "1st"))
    print(time.time() - s)

    s = time.time()
    print(counting_stuff("PClass", "1st"))
    print(time.time() - s)


# speed_test(df)

#print(counting_ppl_the_other_way(df, "PClass", "1st", 0))
#  ^ Ostatni argument jest opcjonlany - 0 w celu oblicznia tyhc któży przeżyli
# through

data1 = data()


def filling_number_of_survivors(df, data1, key, dff, keyy, keyy_value, survived=3):
    data1.adding_data(key, counting_ppl_the_other_way(
        dff, keyy, keyy_value, survived))


def filling_number_of_survivors_with_paratr(df, data1, key, keyy, key_value, key_value1, key_value2, survived=3):
    data1.adding_data(key, count_ppl_the_other_way_with_paratr(
        keyy, key_value, key_value1, key_value2, survived=3))  # here


def filling_number_of_passengers(df):
        data1.number_of_passengers = 1313
        data1.number_of_passengers_in_1stclass = counting_ppl_the_other_way(df,"PClass","1st")
        data1.number_of_passengers_in_2ndclass = counting_ppl_the_other_way(df,"PClass", "2nd")
        data1.number_of_passengers_in_3rdclass = counting_ppl_the_other_way(df,"PClass", "3rd")
        data1.number_of_passengers_that_were_male = counting_ppl_the_other_way(df,"Sex","male")
        data1.number_of_passengers_that_were_female = counting_ppl_the_other_way(df,"Sex","female")

        data1.number_of_passengers_that_were_below_age18 = count_ppl_the_other_way_with_paratr("Age","NaN",0,18)
        data1.number_of_passengers_that_were_below_age60 = count_ppl_the_other_way_with_paratr("Age","NaN",0,60)
        data1.number_of_passengers_between_age18and60 = count_ppl_the_other_way_with_paratr("Age","NaN",19,60)
        
# wszyscy
"""
filling_number_of_survivors(
    df, data1, 'number_of_survivors', df, 'Survived', 1, 3)
print(data1.number_of_survivors)
"""


def collecting_all_data():
    filling_number_of_survivors(
        df, data1, 'number_of_survivors', df, 'Survived', 1, 3)
    filling_number_of_survivors(
        df, data1, 'number_of_surviors_that_were_male', df, 'Sex', 'male', 0)
    filling_number_of_survivors(
        df, data1, 'number_of_surviors_that_were_female', df, 'Sex', 'female', 0)
    filling_number_of_survivors(
        df, data1, 'number_of_surviors_in_1stclass', df, 'PClass', '1st', 0)
    filling_number_of_survivors(
        df, data1, 'number_of_surviors_in_2ndclass', df, 'PClass', '2nd', 0)
    filling_number_of_survivors(
        df, data1, 'number_of_surviors_in_3rdclass', df, 'PClass', '3rd', 0)
    filling_number_of_survivors_with_paratr(
        df, data1, 'number_of_survivors_that_were_below_age18', 'Age', 'NaN', 0, 18, 0)
    filling_number_of_survivors_with_paratr(
        df, data1, 'number_of_survivors_that_were_below_age60', 'Age', 'NaN', 0, 60, 0)
    filling_number_of_survivors_with_paratr(
        df, data1, 'number_of_surviors_between_age18and60', 'Age', 'NaN', 19, 60, 0)


collecting_all_data()
filling_number_of_passengers(df)

"""
print(data1.number_of_survivors)
print(data1.number_of_surviors_that_were_male)
print(data1.number_of_surviors_in_1stclass)
print(counting_ppl_the_other_way(df, 'PClass', '1st', 0))
print(data1.number_of_surviors_between_age18and60)
"""
print(data1.number_of_passengers_that_were_female)
print(data1.number_of_surviors_that_were_female)
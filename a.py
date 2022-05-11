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
                if self.Age == key_value:
                    return 1
                else:
                    return 0
            case 'Sex':
                if self.Sex == key_value:
                    return 1
                else:
                    return 0
            case 'Survived':
                if self.Sex == key_value:
                    return 1
                else:
                    return 0


class data:
    def __init__(self):
        self.number_of_survivors
        self.number_of_survivors_that_were_below_age18
        self.number_of_survivors_that_were_below_age60
        self.number_of_surviors_between_age18and60
        self.number_of_surviors_that_were_male
        self.number_of_surviors_that_were_female
        self.self.number_of_surviors_in_1stclass
        self.self.number_of_surviors_in_2ndclass
        self.self.number_of_surviors_in_3rdclass




pd.options.display.max_rows = 10

df = pd.read_csv('titanic\Titanic.csv')


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


def counting_ppl_the_other_way(df, key, key_value, survived=3):  # szybsze
    amm = 0
    for _ in range(len(df)):
        amm = amm + objs[_].count_ppl_the_other_way(key, key_value, survived)
    return amm


def speed_test(df):
    s = time.time()
    print(counting_ppl_the_other_way(df, "PClass", "1st"))
    print(time.time() - s)

    s = time.time()
    print(counting_stuff("PClass", "1st"))
    print(time.time() - s)


# speed_test(df)

print(counting_ppl_the_other_way(df, "PClass", "1st", 0))
#  ^ Ostatni argument jest opcjonlany - 0 w celu oblicznia tyhc któży przeżyli

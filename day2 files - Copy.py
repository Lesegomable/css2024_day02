# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 09:53:50 2024

@author: muamb
"""


import pandas as pd

file = pd.read_csv("data_02/iris.csv")

abc=1

if=2
$fi=3
_public=4
bob's=6
if=2
emp id=8


file = pd.read_csv("data_02/Geospatial Data.txt",sep=";")
file = pd.read_csv(".spyproject/data_02/patient_data.csv")

file = pd.read_excel(".spyproject/data_02/residentdoctors.xlsx")

print(file)

file = pd.read_json(".spyproject/data_02/student_data.json")
print(file)
file = pd.read_txt(".spyproject/data_02/Geospatial Data.txt")

#csv data is separated with commas 

file = pd.read_csv(".spyproject/data_02/Geospatial Data.txt",sep=";")
print(file)

#objects are strings which are words. 

file = pd.read_excel(".spyproject/data_02/residentdoctors.xlsx")
print(file)
print(file.info())

#to makea column from the existing one
file["LOWER_AGE"] = file["AGEDIST"].str.extract('(\d+)-')
print(file)
print(file.info())

#Convert from string to interger to remove object

file["LOWER_AGE"] = file["LOWER_AGE"].astype(int)
print(file)
print(file.info())

x = [1,2,3]
y = x[1:]
print(y)

x = {'a': 1, 'b': 2}
x.update({'c': 3})
print(x)

x = {'a': 1, 'b': 2}
del x['a']
print(x)

x.get(key)


# remove a non number value
file.dropna(inplace = true)
file.reset_index(drop=True)


import pandas as pd

import pandas as pd

file = pd.read_csv("data_02/iris.csv")
file = pd.read_csv(".spyproject/data_02/iris.csv")

col_names = file.columns.tolist()
print(file)
print(file.info())
file["sepal_length_sq"] =  file["sepal_length"]**2


grouped = file.groupby("class")

mean_square_values = grouped['sepal_length_sq'].mean()
print(mean_square_values)


file1 = pd.read_scv(".spyproject/data_02/person_split1.csv")
file2 = pd.read_scv(".spyproject/data_02/person_split2.csv")




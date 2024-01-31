# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



import pandas

file = pandas.read_csv("country_data.csv")

print(file)


print(file.info())


print(file.describe())

import pandas



file = pandas.read_csv("iris.csv")


print(file)

print(file.info())

print(file.describe())

file=pandas.read.csv('insurance_data.csv'skiprows=5)

column_names=["A","B","C","D","E","F","G","H","I","J","K","K","L","M","N"]

file=pandas.read_csv("housing_data.csv")

print(file.info())

print(file.describe())

file=pandas.read_csv('housing_data.csv',names=column_names)

print(files)



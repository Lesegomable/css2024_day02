# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:40:54 2024

@author: muamb
"""


storing data in python
1. Lists
2. Dictinaries
3. Data frames - specific to pandas

import pandas

file = pandas.read_csv("country_data.csv")

print(file)

  Age Gender       Country
0    39      M  South Africa
1    25      M      Botswana
2    29      F  South Africa
3    46      M  South Africa
4    22      F         Kenya
5    35      F    Mozambique
6    22      F       Lesotho
7    49      M         Kenya
8    30      M         Kenya
9    40      F         Egypt
10   30      M         Sudan

age1 = 30
age2 = 25
age3 = 29 

age =[30,25,29,46,22]

print(age)

[30, 25, 29, 46, 22]

print(age[0])

print(age[1])

print(sum(age))
    
print(len(age))

C2 = "M"
C3 = "M"
C4 = "F" 

print(C2)
print(C3)
print(C4)

# gender list
gender = ["M","M","F","M","F","F","F","M","M","F","M"]

print(gender[0])
# gender list
gender = ["M","M","F","M","F","F","F","M","M","F","M"]
print(gender[2])
print(gender[-1])



# country list
country = ["South Africa","Botswana","South Africa","South Africa","Kenya","Mozambique","Lesotho","Kenya","Kenya","Egypt","Sudan"]

country = ["South Africa","Botswana","South Africa","South Africa","Kenya","Mozambique","Lesotho","Kenya","Kenya","Egypt","Sudan"]

print(country)
print(country[0])
print(country[4])


#Dictinaries- key:value pairs
cat : "a cute animal"

mammals = {"cat" : "a cute animal" , "a lion" : "king of the jugle" , "elephant" : "a gigantic beast"}
print(mammals["cat"])



#Data frames


fruits = ["apple" , "banana" , "orange" , "grape"]
size_nm = [9.8, 10.1, 13.2, 20.5, 8.7]

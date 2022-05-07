# -*- coding: utf-8 -*-
"""Pandas_excercise_214520.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TNoK_R0PXoTVnGGQEWablSKRdddBeGRl
"""

import pandas as pd
import numpy as np

my_data = np.array([ [1,'Kevin',20] , [2,'Sobak',18] , [3,'Alloy',3] ])

column_names = ['Regstr.' , 'Name' , 'Marks']

my_dataframe = pd.DataFrame(data = my_data , columns = column_names)

print(my_dataframe)

my_dataframe['Grades'] = ['A' , 'B' , 'C']

print(my_dataframe)

#Printing anyone row
print(my_dataframe.iloc[[2]],'\n')

#Printing some rows from the top
print(my_dataframe.head(2),'\n')

#printing a particular column
print(my_dataframe['Name'],'\n')

#Printing from a certain row to another
print(my_dataframe[1:3],'\n')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

from google.colab import drive
drive.mount('/content/drive',force_remount= True)
data = pd.read_csv("Shark_Tank_India_S1_new.csv")

data

data.head()

data.tail()

data.shape

data.columns

data.isnull().sum()

"""trying different functions of pandas using various dataframes for samples

"""

person = pd.DataFrame({'Name':['Asif' , 'Basit' , 'John', 'Hary'],
 'DOB': ['3/20/1960', '3/19/1981', '9/12/1999' , '7/12/1967'],
 'EmpID': ['E453', 'E983', 'E675','E120']})

person['DOB']=pd.to_datetime(person['DOB'])
print(person['DOB'])

from datetime import date

a = pd.Timestamp(date(1980,12,20))
print(a)



"""Various ways to make a dataframe

"""

df2 = pd.DataFrame({ 'A' : 1.,
'B':pd.Timestamp('20130102'),
'C':pd.Series(1.5,index=list(range(4))),
'D':np.array([3] * 4),
'E':pd.Categorical(["test","train","test","train"]),
'F':'foo' })

print(df2)

dates = pd.date_range("20220401", periods=4)

df = pd.DataFrame(np.random.randn(4,4), index=dates, columns=list('ABCD'))
df




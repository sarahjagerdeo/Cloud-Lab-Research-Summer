import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np

#**********************************************************************
#List to store the data (ADD AS MUCH AS NECESSARY)
#**********************************************************************

xlist = []
x1list = []
ylist = []
zlist = []

#**********************************************************************
#File Read
#fname : put the name of the file you are reading 
#**********************************************************************

#fname = "const_svc_cost_c20"
#df = pd.read_csv(r'/Users/sarahjagerdeo/Desktop/web-bench/dog-days-university-loadtest/input/{}.csv'.format(fname))

#If you only want a certain number of rows put in the number of rows you want with n = ?
#------------------------------------------------------------------------------------

#df = pd.read_csv(r'/Users/sarahjagerdeo/Desktop/web-bench/dog-days-university-loadtest/input/{}.csv'.format(fname), nrows = (a number) )
#print(df)

#----------------------------------
#If you have no column names and or txt file
#fname : put the name of the file you are reading 
#----------------------------------
# fname = "rDist"
# df = pd.read_csv(r'/Users/sarahjagerdeo/Desktop/web-bench/dog-days-university-loadtest/input/{}.txt'.format(fname), header= None)


#dr.columns will give the data a column name, you can add names for all columns as needed
#----------------------------------------------
# df.columns = ['Random1']

# Updated.txt will ouput a txt file updated with column name
#----------------------------------------------
#df.to_csv('/Users/sarahjagerdeo/Desktop/web-bench/dog-days-university-loadtest/input/Updated.txt')
#**********************************************************************


#**********************************************************************
#Print all Column headings
# for col in df.columns:
#     print(col)
#**********************************************************************

#**********************************************************************
#df.iterrows returns series for each row it does not preserve data types across the rows
#iterate through the rows and take the data with it and append it to lists to use
#---------------------------------------------------------------------------------
# for index, row in df.iterrows():
#         xlist.append(index)
#         #put header name of data you want in the hard brackets
#         ylist.append(row['Random1'])

#       
#---------------------------------------------------------------------------------
#**********************************************************************

#--------------------------
#Line plot function
#--------------------------
# def plot (x,y1):
#     plt.plot(x, y1, label = "line 1")
#     plt.show()
# plot(xlist,ylist)
#--------------------------
 
#--------------------------
#Histogram
#--------------------------
# plt.title('Random Distribution')
# plt.xlabel('categories')
# plt.ylabel('values')
# plt.hist(ylist, density=True, bins=30)
# plt.show()
#--------------------------

#--------------------------
#Bar Plot
#--------------------------
#plt.bar(xlist,ylist)
#plt.show()
#--------------------------


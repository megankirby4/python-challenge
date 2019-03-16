#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import os


# In[2]:


#import csv file
bank_data_file = "PyBankData.csv"


# In[3]:


#read and display csv file in data frame
bank_data_file_pd = pd.read_csv(bank_data_file)
bank_data_file_pd


# In[4]:


#Calculate the number of months in the data frame
number_of_months = bank_data_file_pd["Date"].count()

print("Total Months: " + str(number_of_months))


# In[5]:


#Calculate the total profits and losses over the entire period
net_total = bank_data_file_pd["Profit/Losses"].sum()

print( "Total Profit/Losses: " + str(net_total))


# In[6]:


#make a list of all the profits/losses from month to month
pl_ToList = list(bank_data_file_pd['Profit/Losses'])

#use numpy to calculate defferences between each months profits/losses
differences = np.diff(pl_ToList)

#use numpy to take the mean of those differences
average = np.average(differences)
average = average.round(2)
average

print( 'Average Change: ' + str(average))


# In[8]:


#Find the greatest increase in profit
max = np.amax(differences)

print("Greatest Increase in Profits: " + "$ " + str(max))


# In[9]:


#Find the greatest decrease in profit
min = np.amin(differences)

print("Greatest Decrease in Profits: " + "$ " + str(min))


# In[10]:


#Print the results

print("Financial Analysis")
print("------------------------------------------")
print("Total Months: " + str(number_of_months))
print( "Total Profit/Losses: " + str(net_total))
print( 'Average Change: ' + str(average))
print("Greatest Increase in Profits: " + "$ " + str(max))
print("Greatest Decrease in Profits: " + "$ " + str(min))


# In[13]:


file = open("PyBank.txt", "w")
file.write("Financial Analysis" + "\n")
file.write("-----------------------------------------------" + "\n")
file.write("Total Months: " + str(number_of_months) + "\n")
file.write("Total Profit/Losses: " + str(net_total) + "\n")
file.write("Average Change: " + str(average) + "\n")
file.write("Greatest Increase in Profits: " + "$ " + str(max) + "\n")
file.write("Greatest Decrease in Profits: " + "$ " + str(min))


# In[ ]:





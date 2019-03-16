#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import os


# In[2]:


#import csv file
file = "ElectionData.csv"


# In[3]:


#Read and display data file into a data frame
election_df = pd.read_csv(file)
election_df.head()


# In[4]:


#Calculate the total number of votes cast based on voter ID (assuming each voter ID counts as one vote)
total_votes = election_df["Voter ID"].count()

print("Total Votes: " + str(total_votes))


# In[5]:


#Make a data frame of the list of candidates and the votes cast for each candidate
cand_votes = election_df["Candidate"].value_counts()
cand_votes_df = pd.DataFrame(cand_votes)
cand_votes_df.columns=["Votes"]

cand_votes_df


# In[6]:


#Make a list of the candidates and votes cast
candidate_list = cand_votes_df.index.tolist()
vote_list = cand_votes_df.iloc[:, 0].tolist()
vote_list


# In[7]:


#Get the percentage of votes per candidate
percent_votes = ((vote_list/total_votes)*100).round(1)
percent_list = list(map("{}%".format, percent_votes))
percent_list


# In[8]:


#Make a data frame of the voting results
results_df = pd.DataFrame({
        "Candidate": candidate_list,
        "Number of Votes": vote_list,
        "Percentage of Votes": percent_list})
results_df


# In[9]:


#Index by number of votes to determine the winner of the election
win_df = results_df.set_index("Number of Votes")
win_votes = max(vote_list)
winner = win_df.loc[win_votes].Candidate
winner


# In[10]:


print("Election Results")
print("---------------------------")
print("Total Votes: " + str(total_votes))
print("------------------------------------")
print(results_df)
print("------------------------------------")
print("Winner: " + str(winner))


# In[15]:


file = open("MeganKirbyPyPoll.txt", "w")
file.write("Election Results" + "\n")
file.write("-----------------------------------------------" + "\n")
file.write("Total Votes: " + str(total_votes) + "\n")
file.write("------------------------------------" + "\n")
file.write(str(results_df) + "\n")
file.write("------------------------------------" + "\n")
file.write("Winner: " + str(winner))


# In[ ]:





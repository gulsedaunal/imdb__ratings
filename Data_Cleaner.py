#author : gulsedaunal
#nov 2015 - insight project
#analysis of the imdb movie ranking data 
#flow : clean - organize - analyze
#part 1 - clean

import sys
import os

#we have ratings.txt file w/ info including:
#num_of_votes, rating, name, release year
#this file has both movies and tv episodes 
#aim : keep movie information only

lineloc = [] # gives the location of the episodes
with open('./Originals/ratings.txt') as input:
    datalist = input.readlines() # store all lines
    input.seek(0) # go back to the start
    for i,line in enumerate(input):
        nline = line.strip()
        nline = nline.split()
        dline = nline[3] # has " for episodes
        if str(dline[0]) == '"':
            lineloc.append(i)

# change episode to empty list element
for item in range(len(lineloc)):
    datalist[lineloc[item]] = ''

with open('./Created/cleaned_data.txt','w') as output:
    output.writelines(datalist)
# cleaned imdb data to keep only movies 
# work with this movie only data

#author : gulsedaunal
#nov 2015 - insight project
#analysis of the imdb movie ranking data 
#flow : clean - organize - analyze
#part 3 - analyze data
import sys
import os

def sort(array):
    less = []
    equal = []
    greater = []
    
    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        return sort(less)+equal+sort(greater)  # join lists
    else:  
        return array

# get all the lists for sorting
year = []
with open('./Created/data2n.txt') as input:
    for i, line in enumerate(input):
        year.append(line)        
votes = []
with open('./Created/data0n.txt') as input:
    for i, line in enumerate(input):
        votes.append(line)
rating = []
with open('./Created/data1n.txt') as input:
    for i, line in enumerate(input):
        rating.append(line)


# for rating vs. year plot
ysorted = sorted(year)
yindex = sorted(range(len(year)), key=lambda k: year[k])
# index sorted according to year 
rsorted1 = [x for (y,x) in sorted(zip(ysorted,rating))]

# for rating vs. year plot
yearsonce = sorted(set(year))
# cannot keep a year more than once

# how many times we see a year (hence votes and ratings for that year)
linetot = []
for line1 in yearsonce:
    counter = 0
    for line2 in ysorted:
        if line2 == line1:
            counter += 1
    linetot.append(counter)

max_rate_pyear = []
min_rate_pyear = []
counter = 0
for line1 in linetot:
    minr = rsorted1[counter]
    maxr = rsorted1[counter+line1-1]
    counter += line1
    max_rate_pyear.append(maxr)
    min_rate_pyear.append(minr)

# save for matlab
with open('./Matlab/yearsonce.csv','w') as output:
    output.writelines(yearsonce)

with open('./Matlab/max_rate_pyear.csv','w') as output:
    output.writelines(max_rate_pyear)

with open('./Matlab/min_rate_pyear.csv','w') as output:
    output.writelines(min_rate_pyear)


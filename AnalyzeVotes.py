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
vsorted = sorted(votes)
yindex = sorted(range(len(year)), key=lambda k: year[k])
vsortedpyear = [x for (y,x) in sorted(zip(ysorted,votes))]

yearsonce = sorted(set(year))

linetot = [] # total num of movies per year
for line1 in yearsonce:
    counter = 0
    for line2 in ysorted:
        if line2 == line1:
            counter += 1
    linetot.append(counter)

total_num_of_movies = linetot
total_num_of_votes = []
counter = 0
for in1, line1 in enumerate(linetot):
    sum_votes = 0
    counter += line1 
    for in2, line2 in enumerate(vsortedpyear):
        if in2 < counter:
            sum_votes += int(line2)
    total_num_of_votes.append(sum_votes)
        
print len(total_num_of_votes)   

    # save for matlab
with open('./Matlab/Detailed/total_num_of_movies.csv','w') as output:
    output.write(str(total_num_of_movies))
    
with open('./Matlab/Detailed/total_num_of_votes.csv','w') as output:
    output.write(str(total_num_of_votes))
#    
with open('./Matlab/Detailed/yearsonce.csv','w') as output:
    output.writelines(yearsonce)
#    

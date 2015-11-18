#author : gulsedaunal
#nov 2015 - insight project
#analysis of the imdb movie ranking data 
#flow : clean - organize - analyze
#part 2 - organize data

import sys
import os


numofvotes = []
ranking = []
years = []

# extract numofvotes (data0) and ranking (data1) from cleaned imdb ranking file
for ind in range(2): # to write both files simultaneously
    with open('./Created/data%i.txt'%ind,'w') as output:
        with open('./Created/cleaned_data.txt') as input:
            for i,line in enumerate(input):
                nline = line.strip()
                nline = nline.split()
                #print nline
                dline = nline[ind+1]
                #print dline
                output.write(dline+'\n')
                if ind == 0:
                    numofvotes.append(nline[ind+1])
                    ranking.append(nline[ind+2])

# the comment-out print lines show the structure of the data:
# ['0000000007', '495', '6.8', 'Zombie', 'Beach', '(2010)']
# ['garbage for us', 'total votes', 'rating', 'name (kind of missleading)', 'year']

print('Total number of movies %d' %len(numofvotes))
# Total number of movies 366313 
# so many movies with too less total number of votes -> can be omitted

# calculate the average number of votes
total = 0
mean = 0
counter = 0
with open('./Created/data0.txt') as input:
    for i, line in enumerate(input):
        total += int(line)
        counter += 1 # total number of movies considered
    mean = total / counter 

print('The average of votes %d' %mean)

#data0 - numofvotes || data1 - rating 
#total number of movies 366313
#let's get rid of the movies with votes less than the mean (this should decrease the error in awards analysis)


# remove the movie info with votes less than mean:
lineloc = []
with open('./Created/data0.txt') as input:
    nlist = input.readlines() # store all lines
    input.seek(0) # go back to start
    for i,line in enumerate(input):
        if int(line) < mean:
            lineloc.append(i) # store loci 
            nlist[i] = ''
#print len(nlist)
with open('./Created/data0n.txt','w') as output:
    output.writelines(nlist)

# remove the ratings:
with open('./Created/data1.txt') as f1:
    f1list = f1.readlines() # store all lines
    f1.seek(0) # go back to start
    for item in range(len(lineloc)):
        f1list[lineloc[item]] = ''
#print len(nlist)
with open('./Created/data1n.txt','w') as output:
    output.writelines(f1list)

with open('./Created/cleaned_data.txt') as input:
    datalist = input.readlines() # store all lines
    input.seek(0) # go back to start
    for item,line in enumerate(input):
        if nlist[item] == '':
            datalist[item] = ''
    
with open('./Created/data2.txt','w') as output:
    output.writelines(datalist)

with open('./Created/data2.txt') as input:
    with open('./Created/data2n.txt','w') as output:
        for i,line in enumerate(input):
            nline = line.split()
            #print nline
            for num in range(3,len(nline)):
                cline = nline[num]
                #print cline
                if cline[1:5].isdigit() and cline[0] == '(':
                    output.write(cline[1:5]+'\n')



# sanity checks:
# compare the sizes of data files:
counter = 0
with open('./Created/data0n.txt') as input:
    for i, line in enumerate(input):
        counter += 1 # total number of movies considered
print counter

counter = 0
with open('./Created/data1n.txt') as input:
    for i, line in enumerate(input):
        counter += 1 # total number of movies considered
print counter

counter = 0
with open('./Created/data2n.txt') as input:
    for i, line in enumerate(input):
        counter += 1 # total number of movies considered
print counter

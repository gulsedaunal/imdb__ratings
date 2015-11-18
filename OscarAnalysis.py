#author : gulsedaunal
#nov 2015 - insight project
#analysis of the imdb movie ranking data 
#flow : clean - organize - analyze
#part 3 -awards- analyze data for oscar awards

import sys
import os
import csv

award_years = range(1928, 2013, 1) # public imdb data set is not up to date
print award_years
print len(award_years)
winners = []
with open('./Originals/oscars.txt') as input:
    datalist = input.readlines() # store all lines
    input.seek(0) # go back to start
    for i, line in enumerate(input):  
        winline = line.split()
        winners.append(winline)  

splitted2 = []
with open('./Created/data2.txt') as input:
    datalist = input.readlines() 
    input.seek(0) 
    for i,line in enumerate(input):
        nline = line.split()
        splitted2.append(nline)
year = []
with open('./Created/data2n.txt') as input:
    for i, line in enumerate(input):
        year.append(line) 
rating = []
with open('./Created/data1n.txt') as input:
    for i, line in enumerate(input):
        rating.append(line)

recordyear = []
with open('./Originals/records.txt') as input:
    for i, line in enumerate(input):
        recordyear.append(line) 
  
#print len(splitted2)
#print len(year)
#print len(rating)

movie_years = []
awarded_ratings = []
registered_movies = [] 
counter1 = -1
for line1 in winners:
    counter1 += 1
    counter2 = -1
    for line2 in splitted2:
        counter2 += 1
        if len(line1) == 1 and line1[0] == line2[3] and recordyear[counter1] == year[counter2]:
            awarded_ratings.append(rating[counter2])
            movie_years.append(year[counter2])
            registered_movies.append(line1)
        elif len(line1) == 2 and line1[1] == line2[4] and (line1[0] == 'A' or line1[0] == 'The')  and recordyear[counter1] == year[counter2]:
            awarded_ratings.append(rating[counter2])
            movie_years.append(year[counter2])
            registered_movies.append(line1)
        elif len(line1) == 2 and line1[0] == line2[3] and line1[1] == line2[4] and line1[0] != 'A' and line1[0] != 'The'  and recordyear[counter1] == year[counter2]:
            awarded_ratings.append(rating[counter2])
            movie_years.append(year[counter2])
            registered_movies.append(line1)
        elif len(line1) >=3 and line1[0] == line2[3] and line1[1] == line2[4] and line1[2] == line2[5] and recordyear[counter1] == year[counter2]:      
            awarded_ratings.append(rating[counter2])
            movie_years.append(year[counter2])
            registered_movies.append(line1)
        else:
            pass 


print len(award_years)
print len(awarded_ratings)
print len(registered_movies)



#### save results for matlab (to plot)
#with open('./Matlab/OscarRatings.csv','w') as output:
#    output.writelines(awarded_ratings)
#
#with open('./Matlab/OscarRecordyear.csv','w') as output:
#    output.writelines(movie_years)

#with open('./Matlab/OscarMovies.csv','w') as output:
#    output.writelines(registered_movies)









        
        
    

# imdb_ratings
1- Data_Cleaner.py: ratings.txt file contains information of: #num_of_votes, rating, name, release year But this file has not only movies but also soap operas, etc. which have ' " ' at the beginning. Here, we try to keep only the movie information.

2- Data_Organizer.py: We extract rating, total votes and release year information.

3- Analyze.py: To extract rating vs. year information.

4- AnalyzeVotes.py: We try to further understand the ratings by looking at the total votes normalized wrt the total movies released for a particular year.

5- OscarAnalysis.py: In order to compare the Oscar Best Picture award winner's rating to the max rating of that year.

IMDB public data set (ratings.txt) is used for the analysis.

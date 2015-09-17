#!/usr/bin/env python

import sys

highRatedUserMovies = {}

for line in sys.stdin:

    data = string.split(line, '::')
    userID = data[0]
    movieID = data[1]
    rating = float(data[2])

    if (rating >= 4.0):
        if highRatedUserMovies.get(userID) == None:
            templist = []
            templist.append(movieID)
            highRatedUserMovies[userID] = templist
        else:
            highRatedUserMovies[userID].append(movieID)

        
#emit users and movies highly rated by them
for key in highRatedUserMovies.keys():
    print key + "\t" + '\t'.join(highRatedUserMovies[key])

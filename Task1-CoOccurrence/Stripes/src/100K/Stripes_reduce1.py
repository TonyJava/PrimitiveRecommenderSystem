#!/usr/bin/env python

import sys

prevUserID = None
userMovieList = []

def addToList(data):
    for item in data:
        userMovieList.append(item)

for line in sys.stdin:

    data = line.strip().split('\t')
    #remove UserID
    userID = int(data.pop(0))

    if prevUserID and (prevUserID != userID):
        #emit sorted movielist
        userMovieList.sort()
        print '\t'.join(userMovieList)
        
        #empty list and start adding new data
        userMovieList = []
        prevUserID = userID
        #userMovieList.extend(data)
        addToList(data)
    else:
        prevUserID = userID
        #userMovieList.extend(data)
        addToList(data)

userMovieList.sort()
print '\t'.join(userMovieList)

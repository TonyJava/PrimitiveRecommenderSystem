#!/usr/bin/env python

import sys

prevMovie = None
dictCoOccurrence = {}
movieNameDictionary = {}

def initializeMovieNames():
    movieFile = open('movies.dat', 'r')
    #print "reading movies.dat"
    for dataline in movieFile:
        #print "*****"
        moviedata = dataline.split('::')
        movieID = int(moviedata[0])
        #print "movieID : " + str(movieID)
        movieName = moviedata[1]
        #print "movieName : " + str(movieName)
        movieNameDictionary[movieID] = movieName

#initializeMovieNames()
for line in sys.stdin:
    data = line.strip().split('\t')
    if not data:
        continue
    currMovieID = int(data.pop(0))
    
    if prevMovie and (prevMovie != currMovieID):
        for key in dictCoOccurrence:
            movieID1, movieID2 = key.split(',')
            print "%d\t%d\t%d" % (int(movieID1), int(movieID2), int(dictCoOccurrence[key]))
            #print "%d\t%d\t%d" % (movieNameDictionary[int(movieID1)], movieNameDictionary[int(movieID2)], int(dictCoOccurrence[key]))
        
        dictCoOccurrence = {}
        
    prevMovie = currMovieID

    #generate the co-occurrence dictionary
    while data:
        key = str(currMovieID) + "," + str(int(data[0]))
        if dictCoOccurrence.get(key) == None:
            dictCoOccurrence[key] = 1
        else:
            dictCoOccurrence[key] += 1            
        data.pop(0)
        
    data = []

for key in dictCoOccurrence:
    movieID1, movieID2 = key.split(',')
    print "%d\t%d\t%d" % (int(movieID1), int(movieID2), int(dictCoOccurrence[key]))
    #print "%d\t%d\t%d" % (movieNameDictionary[int(movieID1)], movieNameDictionary[int(movieID2)], int(dictCoOccurrence[key]))
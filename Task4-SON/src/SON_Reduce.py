#!/usr/bin/env python

import sys

MIN_SUPPORT = 1400

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

finalOutput = {}

def addToFinalOutput(candidateSet, count):
    if finalOutput.get(candidateSet) == None:
        finalOutput[candidateSet] = 0
    else:
        finalOutput[candidateSet] += count

def readInput():
    for line in sys.stdin:
        data = line.split('\t')
        candidateSet = (data[0])
        count = int(data[1])
        addToFinalOutput(candidateSet, count)
        
def emitFinalOutput():
    #ignore finalOutput lower than threshold
    for key in finalOutput.keys():
        if int(finalOutput[key]) < MIN_SUPPORT:
            continue
        else:
            movieIDs = key.split(",")
            #print movieNames and its Support
			for movieID in movieIDs:
                print movieNameDictionary[int(movieID)]
            print "Support Count = %d" % finalOutput[key]
            
def main():
    initializeMovieNames()
    readInput()
    emitFinalOutput()

if __name__ == "__main__":
    main()
#! /usr/bin/env python
'''
Created on Mar 10, 2015
@author: Jatin
'''

import sys

#RECORDS_CNT = 100000
nTotalUsers = 0
movieNameDictionary = {}
highRatedMovieDictionary = {}

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

def initializeHighRatings():
    occurrencesFile = open('part-00000', 'r')
    #print "reading Occurrence.dat"
    for occurenceline in occurrencesFile:
        #print "-----"
        occurencedata = occurenceline.split('\t')
        movieID = int(occurencedata[0])
        #print "movieID : " + str(movieID)
        nOccur = int(occurencedata[1])
        #print "nOccur : " + str(nOccur)
        highRatedMovieDictionary[movieID] = nOccur

def main():
    #print "initializeMovieNames..."
    initializeMovieNames()
    #print "initializeHighRatings..."
    initializeHighRatings()
    
    userCntFile = open('userCount.dat', 'r')
    #print "reading Occurrence.dat"
    for userCount in userCntFile:
        data = userCount.split()
        nTotalUsers = int(data[0])
    #print str(nTotalUsers)
    
    #inputfile = open('part-00000', 'r')
    for line in sys.stdin:
        #print "======================================================================="
        data = line.split('\t')
        movieID1 = int(data[0])
        #print "movieid1 : " + str(movieID1)
        movieID2 = int(data[1])
        #print "movieid2 : " + str(movieID2)
        nCoOccurrence = int(data[2])
        #print "Co occurrence count : " + str(nCoOccurrence)
        
        nMovie1Occur = highRatedMovieDictionary[movieID1]
        #print "Movie1 occur total : " + str(nMovie1Occur)
        nMovie2Occur = highRatedMovieDictionary[movieID2]
        #print "Movie2 occur total : " + str(nMovie2Occur)
        
        #print "Total USers: " + str(nTotalUsers)
        #nNum = float(nCoOccurrence*nTotalUsers)
        #nDen = float(nMovie1Occur*nMovie2Occur)
        lift = float(nCoOccurrence*nTotalUsers)/(nMovie1Occur*nMovie2Occur)
        #lift = float(nCoOccurrence * RECORDS_CNT)/(nMovie1Occur * nMovie2Occur)
        #print "lift : " + str(lift)
        #=======================================================================
        # if (lift >= 1.5):
        #     movieName1 = movieNameDictionary[movieID1]
        #     movieName2 = movieNameDictionary[movieID2]
        #     print '%f\t%s\t%s' % (lift, movieName1, movieName2)
        #=======================================================================
        if (lift >= 1.5):    
            movieName1 = movieNameDictionary[movieID1]
            movieName2 = movieNameDictionary[movieID2]
            print '%f\t%s\t%s' % (lift, movieName1, movieName2)        

if __name__ == "__main__":
    main()

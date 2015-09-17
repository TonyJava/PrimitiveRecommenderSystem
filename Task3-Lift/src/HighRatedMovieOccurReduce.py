#! /usr/bin/env python
'''
Created on Mar 10, 2015
@author: Jatin
'''

import sys

prevMovieID = None
nTotalOccurrences = 0

#get each line from input
for line in sys.stdin:
    data = line.split('\t')

    movieID = int(data[0])
    likes = int(data[1])
    #nTotalUsers = int(data[3])
    
    #emit movieID as we have accumulated its total Occurrence
    if prevMovieID and (prevMovieID != movieID):
        print '%d\t%d' % (prevMovieID, nTotalOccurrences)
        #print '%d\t%d\t%d' % (prevMovieID, nTotalOccurrences, nTotalUsers)
        nTotalOccurrences = 0
        
    prevMovieID = movieID
    nTotalOccurrences += likes

#emit last movieId
print '%d\t%d' % (prevMovieID, nTotalOccurrences)
#print '%d\t%d\t%d' % (prevMovieID, nTotalOccurrences, nTotalUsers)
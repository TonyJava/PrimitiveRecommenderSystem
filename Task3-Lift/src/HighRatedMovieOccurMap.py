#! /usr/bin/env python
'''
Created on Mar 10, 2015
@author: Jatin
'''

# Reads the ratings.dat file

import sys

highRatedMovieCount = {}
#lstUser = []

def addToDictionary(movieId):
    if highRatedMovieCount.get(movieId) == None:
        highRatedMovieCount[movieId] = 1
    else:
        highRatedMovieCount[movieId] += 1

'''        
def addUserToUniqueList(userId):
    if userId in lstUser:
        return
    else:
        lstUser.append(userId)
'''
        
def emitHighRatedMovieOccurrences():
    #nUserLstCnt = len(lstUser)
    for movieId in highRatedMovieCount:
        nOcuurences = highRatedMovieCount[movieId]
        print '%d\t%d' % (movieId, nOcuurences)
        #print '%d\t%d\t%d' % (movieId, nOcuurences, nUserLstCnt)

for line in sys.stdin:
    userId = -1 # default sorted as first
    movieId = -1 # default sorted as first
    rating = -1 # default sorted as first
    
    #remove any leading or trailing whitespace
    line = line.strip()
    data = line.split('::') # Read the input from STDIN 
    userId = int(data[0])
    movieId = int(data[1])
    rating = data[2]        
    if float(rating) >= 4.0: # For every movie rated highly
        addToDictionary(movieId)
        #addUserToUniqueList(userId)

emitHighRatedMovieOccurrences()
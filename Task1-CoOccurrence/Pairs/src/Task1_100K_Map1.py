#! /usr/bin/env python
'''
Created on Mar 8, 2015
@author: Jatin
'''

import sys

for line in sys.stdin:
    userId = -1 # default sorted as first
    movieId = -1 # default sorted as first
    rating = -1 # default sorted as first
    
    #remove any leading or trailing whitespace
    line = line.strip()
    
    data = line.split('\t') # Read the input from STDIN 
    userId = data[0]
    movieId = data[1]
    rating = data[2]
    if int(rating) >= 4: # For every movie rated highly
        print userId + "\t" + movieId # emit(key,value)
    
    '''
    try:
        data = line.split('\t') # Read the input from STDIN 
    
        userId = data[0]
        movieId = data[1]
        rating = data[2]
        
        if int(rating) >= 4: # For every movie rated highly
            print userId + "\t" + movieId # emit(key,value)
    except: # Any errors which may make your job fail
        pass
'''
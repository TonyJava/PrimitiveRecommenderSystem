#! /usr/bin/env python
'''
Created on Mar 10, 2015
@author: Jatin
'''

import sys

for line in sys.stdin:
    data = line.split('\t')
    movieID1 = int(data[0])
    movieID2 = int(data[1])
    nOccurrence = int(data[2])
    print '%d\t%d\t%d' % (movieID1, movieID2, nOccurrence)
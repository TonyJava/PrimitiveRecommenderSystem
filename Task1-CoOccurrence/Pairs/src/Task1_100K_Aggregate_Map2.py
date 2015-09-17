#! /usr/bin/env python
'''
Created on Mar 8, 2015
@author: Jatin
'''

import sys

for line in sys.stdin:
    line = line.strip()
    data = line.split("\t")
    for i in range(1,len(data)):
        for j in range(i + 1,len(data)):
            if i != j:
                pair = sorted([int(data[i]), int(data[j])])
                print "LongValueSum:" + str(pair[0]) + "\t" + str(pair[1]) + "\t" +"1"

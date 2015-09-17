#! /usr/bin/env python
'''
Created on Mar 10, 2015
@author: Jatin
'''

import sys

for line in sys.stdin:
    line = line.strip()
    
    data = line.split('\t')
    data_len = len(data)
    for movid1 in range(1,data_len):
        for movid2 in range(1,data_len):
            if movid1 != movid2:
                moviePair = sorted([data[movid1], data[movid2]])
                # emit actual movie moviePair
                print moviePair[0] + "\t" + moviePair[1] + "\t" + "1" 
                # emit special key pairs
                #print moviePair[0] + "\t" + "*" + "\t" + "1" 
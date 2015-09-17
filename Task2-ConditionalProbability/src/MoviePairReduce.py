#! /usr/bin/env python
'''
Created on Mar 10, 2015
@author: Jatin
'''

import sys

totalMov1 = 0
total = 0
prevKey = False
for line in sys.stdin:
    line = line.strip()
    data = line.split('\t')
    currentKey = '\t'.join(data[:2])
    count = int(data[2])
    
    if prevKey and currentKey != prevKey: 
        if (prevKey.split('\t'))[1] != "*":
            condProb = float(total)/totalMov1
            if condProb > 0.8:
                print prevKey + "\t" + '%0.10f' % float(condProb)
        else: # Special key encountered
            totalMov1 = total
        prevKey = currentKey
        total = count
    else:
        prevKey = currentKey
        total += count

# emit last key
if prevKey:
    condProb = float(total)/totalMov1
    if condProb > 0.8:
        print prevKey + "\t" + '%0.10f' % float(condProb)

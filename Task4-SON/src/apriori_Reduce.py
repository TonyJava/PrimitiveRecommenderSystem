#!/usr/bin/env python

import sys

frequentSet = set()
dictFreqSets = {}

def addToDict(frozenFreqSet, count):
    if dictFreqSets.get(frozenFreqSet) == None:
        dictFreqSets[frozenFreqSet] = count
    else:
        dictFreqSets[frozenFreqSet] += count

for line in sys.stdin:
    data = line.split()
    frequentSet.add(data[0])
    count = int(data[1])
    frozenFreqSet = frozenset(frequentSet)
    addToDict(frozenFreqSet, count)

for item in dictFreqSets:
    freqItems = ",".join(item)
    print '%s\t%d' % (freqItems, dictFreqSets[item])

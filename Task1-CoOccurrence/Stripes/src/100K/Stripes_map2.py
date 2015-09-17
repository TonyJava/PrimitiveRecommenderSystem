#!/usr/bin/env python

import sys

for line in sys.stdin:
    data = line.strip().split('\t')
    #print data
    while data:
        print '\t'.join(data)
        #pop first value off the list
        data.pop(0)
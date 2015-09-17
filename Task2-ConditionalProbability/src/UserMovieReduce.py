#! /usr/bin/env python
'''
Created on Mar 10, 2015
@author: Jatin
'''

import sys
from itertools import groupby

def disp(data):
    for key,group in groupby(data,lambda x:x[0]):
        try:
            values = "\t".join([value[1] for value in group])
            print key + "\t" + values
        except ValueError:
            pass

def readInput(inputFile, separator='\t'):
    for line in inputFile:
        yield line.rstrip().split(separator, 1)

def main():
    data = readInput(sys.stdin, '\t')
    disp(data)

if __name__ == "__main__":
    main()

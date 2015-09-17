#! /usr/bin/env python
'''
Created on Mar 8, 2015
@author: Jatin
'''

import sys

def load_file(filePath):
    movieDict = {}
    f = open(filePath,'r')
    
    for line in f:
        line = line.strip()
        line = line.split('|')
        key = line[0]
        value = line[1]
        movieDict[key] = value
    return movieDict

def main():
    dictionary = load_file('u.item')

    for line in sys.stdin:
        line = line.strip()
        data = line.split('\t')
        
        try:
            print data[2] + "\t" + dictionary[data[0]] + "\t" + dictionary[data[1]]
        except ValueError:
            pass

if __name__ == "__main__":
    main()

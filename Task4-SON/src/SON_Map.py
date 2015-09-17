#!/usr/bin/env python

#calculate item counts in basket using candidate itemsets

import sys

lstBasket = []
dictCandidates = {}

def initializeCandidates():
    #read the candidate file
    fileCandidates = open('candidateItemSets.dat', 'r')
    for line in fileCandidates:
        
        newCandidateSet = set()
        data = line.strip().split('\t')
        
        freqItems = data[0]
        itemsCount = int(data[1])
        
        items = freqItems.split(',')
        
        for item in items:
            newCandidateSet.add(int(item))
        
        newCanddateSetKey = frozenset(newCandidateSet)
        
        #setting zero here as we need to check in our baskets whether its still a valid candidate
        dictCandidates[newCanddateSetKey] = 0

def readBaskets():
    #read baskets of movieIDs from input
    for line in sys.stdin:
        movieIDs = line.split('\t')
    
        #save each movieID into a Basket which is a set to ensure no repetitions
        setBasket = set()
        for movieID in movieIDs:
            setBasket.add(int(movieID))
    
        #add this Basket to a list of Baskets
        lstBasket.append(setBasket)

def calcCandidateCounts():
    #loop through all the candidates in each basket and check if that candidate is a subset of that basket.
    #If yes then increment the candidate's count in the dictionary
    for candidate in dictCandidates:
        for setBasket in lstBasket:
            #check if current candidate in Basket
            if candidate.issubset(setBasket):
                dictCandidates[candidate] += 1

def emitData():
    #emit
    for candidate in dictCandidates.keys():
        print ','.join(map(str, list(candidate))) + "\t" + str(dictCandidates[candidate])

def main():
    initializeCandidates()
    readBaskets()
    calcCandidateCounts()
    emitData()

if __name__ == "__main__":
    main()
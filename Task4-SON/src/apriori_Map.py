#!/usr/bin/env python

import os, sys, operator
from itertools import chain

try:
    from collections import defaultdict
except:
    class defaultdict(dict):
        def __init__(self, default_factory=None, *a, **kw):
            if (default_factory is not None and
                not hasattr(default_factory, '__call__')):
                raise TypeError('first argument must be callable')
            dict.__init__(self, *a, **kw)
            self.default_factory = default_factory
        def __getitem__(self, key):
            try:
                return dict.__getitem__(self, key)
            except KeyError:
                return self.__missing__(key)
        def __missing__(self, key):
            if self.default_factory is None:
                raise KeyError(key)
            self[key] = value = self.default_factory()
            return value
        def __reduce__(self):
            if self.default_factory is None:
                args = tuple()
            else:
                args = self.default_factory,
            return type(self), args, None, None, self.items()
        def copy(self):
            return self.__copy__()
        def __copy__(self):
            return type(self)(self.default_factory, self)
        def __deepcopy__(self, memo):
            import copy
            return type(self)(self.default_factory,
                              copy.deepcopy(self.items()))
        def __repr__(self):
            return 'defaultdict(%s, %s)' % (self.default_factory,
                                            dict.__repr__(self))


def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = range(r)
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

nLineCount = 0

def readFile():
    nLineCount = 0
    for line in sys.stdin:
        if nLineCount >= 100:
            break
        line = line.strip()
        if line:
            nLineCount += 1
            vals = line.split('\t')
            del vals[0]
            line2 = '\t'.join(vals)
            if line2:
                yield line2.split('\t')
    
def generateCandidates(frequentSet, itemGroupSize):
    """
    Generate candidate set of size itemGroupSize from the previously frequent itemsets
    :param frequentSet:
    :param itemGroupSize:
    :return: candidateSet
    """
    #print 'Generating Candidates for itemGroupSize - %s' % (itemGroupSize)
    if itemGroupSize == 1:
        return frequentSet

    result = []
    expandedItems = set([item for tup in frequentSet for item in tup])

    itemCombinations = chain(*[combinations(expandedItems, itemGroupSize)])
    for itemCombination in itemCombinations:
        subsetCombinations = chain(*[combinations([item for item in itemCombination], itemGroupSize - 1)])
        allSubsetsFrequent = True
        for subset in subsetCombinations:
            if tuple(sorted(subset)) not in frequentSet:
                allSubsetsFrequent = False
        if allSubsetsFrequent:
            result.append(tuple(sorted(itemCombination)))
    return result


def getFrequency(candidateSet, transactionList, itemGroupSize):
    #print 'Fetching frequency for candidate set of size - %s' % (len(candidateSet))
    itemsetFrequency = defaultdict(int)
    for transaction in transactionList:
        itemCombinations = chain(*[combinations(transaction, itemGroupSize)])
        for itemCombination in itemCombinations:
            if tuple(sorted(itemCombination)) in candidateSet:
                itemsetFrequency[tuple(sorted(itemCombination))] += 1
    return itemsetFrequency


def generateFrequentSet(candidateSetFrequency, minSupport):
    #print 'Generating Frequent Item Sets\n\n'
    result = {}
    for item, frequency in candidateSetFrequency.iteritems():
        #print "freq : " + str(frequency)
        #print "item : " + str(item)
        if frequency >= minSupport:
            result[tuple(sorted(item))] = frequency
    return result


if __name__ == '__main__':
    #dataFile = sys.argv[1]
    #dataFile = sys.stdin
    #minSupport = int(sys.argv[3])
    nLineCount = 0
    minSupport = 500
    frequentItemSets = {}
    transactionList = []
    frequentSet = set()

    for transaction in readFile():
        transactionList.append(transaction)
        for item in transaction:
            frequentSet.add(item)
        #print frequentSet

    itemGroupSize = 1
    stoppingCondition = False
    
    #print frequentSet
    frequentSet = [itemset for itemset in chain(*[combinations(frequentSet, 1)])]
    #for itemset in chain(*[combinations(frequentSet, 1)]):
    #    print itemset

    while not stoppingCondition:
        candidateSet = generateCandidates(frequentSet, itemGroupSize)
        candidateSetFrequency = getFrequency(candidateSet, transactionList, itemGroupSize)
        frequentSet = generateFrequentSet(candidateSetFrequency, minSupport)
        if not frequentSet:
            stoppingCondition = True
        else:
            frequentItemSets[itemGroupSize] = frequentSet
            frequentSet = set(frequentSet.keys())
        itemGroupSize += 1

    finalOutput = defaultdict(list)
    
    for key, value in frequentItemSets.iteritems():
        for k, v in value.iteritems():
            finalOutput[v].append(','.join(k))

    print finalOutput
    sortedOp = sorted(finalOutput.items(), key=operator.itemgetter(0), reverse=True)
    for i in sortedOp:
        for item in sorted(i[1]):
            print item + '\t' + str(i[0])
    '''
    with open(sys.argv[2], 'w') as outFile:
        for key, value in frequentItemSets.iteritems():
            for k, v in value.iteritems():
                finalOutput[v].append(' '.join(k))


        sortedOp = sorted(finalOutput.items(), key=operator.itemgetter(0), reverse=True)
        for i in sortedOp:
            for item in sorted(i[1]):
                print item + '\t(' + str(i[0]) + ')'
                outFile.write(item + '\t(' + str(i[0]) + ')\n')
    '''

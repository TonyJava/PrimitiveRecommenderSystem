#! /usr/bin/env python

import sys

prevUser = None
nTotal = 0

for line in sys.stdin:
    currentUser = line
    if (prevUser != currentUser):
        nTotal += 1
    prevUser = currentUser
print '%d' % (nTotal)
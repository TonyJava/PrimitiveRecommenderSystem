#! /usr/bin/env python

import sys

Users = {}

for line in sys.stdin:
    data = line.split('::')
    userId = int(data[0])

    if userId not in Users:
        Users[userId] = 1

for user in Users:
    print '%d' % (user)
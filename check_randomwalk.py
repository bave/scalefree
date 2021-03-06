#!/usr/bin/env python

# sys.argv[1] is topology filename
# sys.argv[2] is gamma value
# sys.argv[3] is random walk times

import sys
import utils
import random
random.seed()

choice = []
test = []
gamma = float(sys.argv[2])

# top2ojb -> topology data to class nodes object in utils.py
nodes = utils.top2obj(sys.argv[1])

for i in nodes.iterkeys():
        choice.append(i)


for i in range(int(sys.argv[3])):
        #print "try :", i
        src=random.choice(choice)
        dst=random.choice(choice)
        print "----- source      :", src,"-----"
        print "----- destination :", dst, "-----"
        path = utils.random_walk(nodes, nodes[src], nodes[dst], gamma)
        test.append(path)

count = 1
for i in test:
    print count, len(i)
    count = count + 1


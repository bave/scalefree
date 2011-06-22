#!/usr/bin/env python
import sys
import utils


# argv[1] is topology file name
nodes=utils.top2obj(sys.argv[1])

cost = []
tmp = 0

keys = nodes.iterkeys()
for i in keys:
    print "start : ", i
    tmp = utils.dijkstra(nodes, nodes[i], None)
    cost.append(tmp)

print cost
print max(cost)

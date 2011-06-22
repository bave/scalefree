#!/usr/bin/env python
import sys
import utils


# argv[1] is topology file name
nodes=utils.top2obj(sys.argv[1])
degree = utils.hash_degree(nodes)
utils.list2file("test_degree", degree)



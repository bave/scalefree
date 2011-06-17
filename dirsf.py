#!/usr/bin/env python
# this program generates directed scale-free graphs
#
# see "Directed scale-free graphs", B. Bollobas, C. Borgs and O. Riordan,
# Proceedings of the 14th Annual ACM-SIAM Symposium on Discrete Algorithms
# (SODA), 132-139 (2003)

import random

class node():
    def __init__(self, id):
        self.inLink  = set()
        self.outLink = set()
        self.id = id
    #end_def
#end_class


class dirsf():

    def __init__(self):
        random.seed()

        self.nodes = {}
        self.nodes[0] = node(0)
        self.nodes[1] = node(1)
        self.nodes[2] = node(2)

        self.nodes[0].outLink.add(1)
        self.nodes[1].inLink.add(0)
        self.nodes[1].outLink.add(2)
        self.nodes[2].inLink.add(1)
        self.nodes[2].outLink.add(0)
        self.nodes[0].inLink.add(2)

        self.edge = 3
        self.n = 2
    #end_def


    def generate(self, step, alpha, beta, din, dout):
        for var in xrange(step):
            rnd = random.random()
            #print self.n
            if rnd < alpha:
                self.n += 1
                fromNode = node(self.n)
                toNode   = self._getNode(din, self._probIn)
                fromNode.outLink.add(toNode.id)
                toNode.inLink.add(fromNode.id)
                self.nodes[self.n] = fromNode
            elif rnd < alpha + beta:
                while True:
                    fromNode = self._getNode(dout, self._probOut)
                    toNode   = self._getNode(din,  self._probIn)
                    if toNode.id in fromNode.outLink:
                        continue
                    #end_if
                    if fromNode.id != toNode.id:
                        fromNode.outLink.add(toNode.id)
                        toNode.inLink.add(fromNode.id)
                        break
                    #end_if
            else:
                self.n += 1
                fromNode   = self._getNode(dout, self._probOut)
                toNode = node(self.n)
                fromNode.outLink.add(toNode.id)
                toNode.inLink.add(fromNode.id)
                self.nodes[self.n] = toNode
            #end_if_elif_else
            self.edge += 1
        #end_for
    #end_def


    def _probIn(self, n, delta):
        din = float(len(self.nodes[n].inLink))
        return (din + delta) / (self.edge + delta * len(self.nodes))
    #end_def



    def _probOut(self, n, delta):
        dout = len(self.nodes[n].outLink)
        return (dout + delta) / (self.edge + delta * len(self.nodes))
    #end_def


    def _getNode(self, delta, prob):
        while True:
            n = int(random.uniform(0, len(self.nodes)))
            rnd = random.random()
            p = prob(n, delta) / len(self.nodes)
            if rnd < p:
                return self.nodes[n]
            #end_if
        #end_while
    #end_def


    def printLink_out(self):
        for n in range(self.n):
            for node in self.nodes[n].outLink:
                print '(%d, %d)' % (n, node)
            #end_for
        #end_for
    #end_def

    def printLink_in(self):
        for n in range(self.n):
            for node in self.nodes[n].inLink:
                print '(%d, %d)' % (n, node)
            #end_for
        #end_for
    #end_def

    def write(self, file):
        fp = open(file, 'w')
        for n in range(self.n):
            for node in self.nodes[n].outLink:
                s = ""
                s += str(n)
                s += " "
                s += str(node)
                s += " "
                s += str(1)
                s += "\n"
                fp.write(s)
                #print '(%d, %d)' % (n, node)
            #end_for
        #end_for
        fp.flush()
        for n in range(self.n):
            for node in self.nodes[n].inLink:
                s = ""
                s += str(n)
                s += " "
                s += str(node)
                s += " "
                s += str(-1)
                s += "\n"
                fp.write(s)
                #print '(%d, %d)' % (n, node)
            #end_for
        #end_for
        fp.flush()
        fp.close()
    #end_def


    # draw with NodeBox
    # see http://nodebox.net/code/index.php/Graph
    def draw(self, width, height):
        try:
            graph = ximport("graph")
        except ImportError:
            graph = ximport("__init__")
            reload(graph)

        size(width, height)
        g = graph.create()

        for n in range(self.n):
            if len(self.nodes[n].outLink) == 0:
                continue
            #end_if
            for id in self.nodes[n].outLink:
                g.add_edge(n, id)
            #end_for

            #for id in self.nodes[n].inLink:
            #    g.add_edge(n, id)
        #end_for

        g.solve()
        g.draw(directed = True, traffic = 1)
    #end_def
#end_class


if __name__ == "__main__":
    # class action check code
    graph = dirsf()
    graph.generate(10, 0.41, 0.59, 0.24, 0.0)
    print "out_Link"
    graph.printLink_out()
    print "in_Link"
    graph.printLink_in()
    #graph.draw(1440, 900)
#end_if


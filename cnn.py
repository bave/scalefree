#!/usr/bin/env python
# this program generates social netwrok graphs by connecting nearest-neighbor
#
# see Alexei Vazquez, "Growing network with local rules: Preferential
# attachment, clustering hierarchy, and degree correlations", Physics Review
# E 67, 2003.

import random


class node:
    def __init__(self, id):
        self.link = []
        self.id = id

class cnn:
    def __init__(self):
        random.seed()

        self.nodes = {}
        self.nodes[0] = node(0)
        self.nodes[1] = node(1)
        self.nodes[2] = node(2)

        self.nodes[0].link = [self.nodes[2]]
        self.nodes[1].link = [self.nodes[2]]

        self.nodes[2].link = [self.nodes[0]]
        self.nodes[2].link = [self.nodes[1]]

        self.neighbor = [(0, 1)]

        self.n = 2


    # create to set max of nodes
    def generate_node(self, step, p):

        while len(self.nodes) < step:
            rnd = random.random()
            if rnd < p:
                self._addLink()
            else:
                self._addNode()

    # crate to set max of steppings
    def generate_step(self, step, p):

        for var in range(step):
            rnd = random.random()
            if rnd < p:
                self._addLink()
            else:
                self._addNode()


    def _addNode(self):
        self.n += 1

        self.nodes[self.n] = node(self.n)

        rnd = int(random.uniform(0, self.n - 1))

        self.neighbor += [(link.id, self.n) for link in self.nodes[rnd].link]

        self.nodes[self.n].link += [self.nodes[rnd]]
        self.nodes[rnd].link    += [self.nodes[self.n]]


    def _addLink(self):
        if len(self.neighbor) == 0:
            return

        rnd = int(random.uniform(0, len(self.neighbor)))
        id1, id2 = self.neighbor[rnd]
        del self.neighbor[rnd]
        
        self.nodes[id1].link += [self.nodes[id2]]
        self.nodes[id2].link += [self.nodes[id1]]

    def printLink(self):
        for n in range(self.n):
            if len(self.nodes[n].link) == 0:
                continue

            for link in self.nodes[n].link:
                if n < link.id:
                    print '(%d, %d)' % (n, link.id)

    def write(self, file):
        fp = open(file, 'w')
        for n in range(self.n):
            if len(self.nodes[n].link) == 0:
                continue
            #end_if
            for link in self.nodes[n].link:
                s = ""
                s += str(n)
                s += " "
                s += str(link.id)
                s += "\n"
                fp.write(s)
                #print '(%d, %d)' % (n, link.id)
            #end_for
        fp.flush()
        fp.close()
        #end_for
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
            if len(self.nodes[n].link) == 0:
                continue

            for link in self.nodes[n].link:
                if n < link.id:
                    g.add_edge(n, link.id)

        g.solve()
        g.styles.apply()
        g.draw(directed = False, traffic = 1)

if __name__ == "__main__":
    graph = cnn()
    graph.generate_node(1000, 0.666)
    graph.printLink()
    graph.write("./test")
    #graph.draw(1280, 800)
#end_if

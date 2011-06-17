#!/usr/bin/env python

import random

class node():
    def __init__(self, id):
        self.id = id
        self.link = []
    #end_def
#end_class

class ba():
    def __init__(self):

        random.seed()

        self.nodes = []


        # initial nodes
        self.nodes.append(node(0))
        self.nodes.append(node(1))
        self.nodes.append(node(2))
        self.nodes[0].link.append(self.nodes[1])
        self.nodes[0].link.append(self.nodes[2])
        self.nodes[1].link.append(self.nodes[0])
        self.nodes[1].link.append(self.nodes[2])
        self.nodes[2].link.append(self.nodes[0])
        self.nodes[2].link.append(self.nodes[1])

        self.init_n = len(self.nodes)
        self.n = self.init_n - 1
        self.add_edge = 2

        if self.n < self.add_edge:
            print "fuck!!"
            return
        #end_if

        return
    #end_def


    def generate(self, number):
        for i in range(number):
            list = []
            list = self._pickup()
            self._add_node(list)
        #end_for
    #end_def


    def _add_node(self, list):
        self.n += 1
        self.nodes.append(node(self.n))
        for i in list:
            self.nodes[self.n].link.append(i)
            i.link.append(self.nodes[self.n])
        #end_for
    #end_def


    def _pickup(self):
        list = []
        op = self._outer_product()
        while 1:
            vatex=random.choice(op)
            try:
                list.index(vatex)
            except ValueError:
                list.append(vatex)
            #end_try
            if len(list) >= self.add_edge:
                break
            #end_if
        #end_while
        return list
    #end_def


    def _outer_product(self):
        list = []
        for i in self.nodes:
            for j in i.link:
                list.append(i)
        return list
    #end_def

    def printLink(self):
        for i in range(self.n):
            if len(self.nodes[i].link) == 0:
                continue
            #end_if
            for j in self.nodes[i].link:
                if i < j.id:
                    print '(%d, %d)' % (i, j.id)
                #end_if
            #end_for
        #end_for
    #end_def

    def write(self,file):
        fp = open(file, 'w')
        for i in range(self.n+1):
            if len(self.nodes[i].link) == 0:
                continue
            #end_if
            for j in self.nodes[i].link:
                s = ""
                s += str(i)
                s += " "
                s += str(j.id)
                s += "\n"
                fp.write(s)
                #print '(%d, %d)' % (i, j.id)
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
        #end_try

        size(width, height)
        g = graph.create(distance=0.5)

        for n in range(self.n):
            if len(self.nodes[n].link) == 0:
                continue
            #end_if

            for link in self.nodes[n].link:
                if n < link.id:
                    g.add_edge(n, link.id)
                #end_if
            #end_for
        #end_for

        g.solve()
        g.draw(directed = False, traffic = 0)
    #end_def
#end_class


if __name__ == "__main__":
    # how to use of this program..
    ba=ba()
    ba.generate(500)
    ba.printLink()
    #ba.write("./test")
    #ba.draw(1280, 800) # this method use only nodebox..
#end_if


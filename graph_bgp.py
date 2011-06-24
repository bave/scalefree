
# this program is for NodeBox..

#file read
links = []
fp = open("caida_test.txt", 'r')

for i in fp:
    tmp = i.split()
    links.append(tmp)

graph = ximport("graph")
size(1280, 800)
g = graph.create(iterations=500,distance=1)

for i in links:
    g.add_edge(i[0], i[1])

g.solve()
g.draw(directed=False,  traffic=0)

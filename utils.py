#!/usr/bin/env python

class node():
  def __init__(self, id):
    #node information
    self.link = []
    self.id = id
  #end_def
#end_class

def random_walk(nodes, src_node, dst_node, gamma):

  import random
  random.seed()
  path = []
  if src_node == dst_node:
    path = [src_node]
    return path
  #end_if

  # initialize
  path.append(src_node)
  next_node = src_node
  prev_node = None
  count = 0

  #while dst_node != next_node and count <= 128:
  while dst_node != next_node:
    link = next_node.link
    link_next = []
    size = 0
    for i in link:
      #print "add link id :", i.id, "->", "link_size :", len(i.link)
      if (len(i.link) == 0):
        print "topology data is conflicte .. !!"
        exit(1);
      #end_if
      weight = len(i.link) ** gamma
      link_next.append((i, weight))
      size += weight

      """
      if i != prev_node and len(i.link) > 1:
        print "add link id :", i.id, "->", "link_size :", len(i.link)
        link_next.append((i, len(i.link)))
        size += len(i.link)
      """

    #end_for

    #print "link_next :",link_next
    #print "link_next size :",size

    #rand=random.randint(0,size)
    rand=random.random() * size

    size = 0.0
    for i in link_next:
      if size <= rand < i[1]+size:
        prev_node = next_node
        next_node = i[0]
        path.append(next_node)
        break
      size += i[1]
    #end_for
    count += 1
    if (count % 1000) == 0:
      #print "random :", rand
      #print "link_next size :",size
      print count, " -> id:", next_node.id
  #end_while
  return path
#end_def

def random_walk_old(nodes, src_node, dst_node):
  import random
  random.seed()
  path = []
  if src_node == dst_node:
    path = [src_node]
    return path
  #end_if

  # initialize
  path.append(src_node)
  next_node = src_node
  prev_node = []
  count = 1

  while next_node != dst_node and count <= 128:
    link = next_node.link
    link_next = []
    for i in link:
      for j in xrange(len(i.link)):
        link_next.append(i)
      #end_for
    #end_for
    #print link_next

    # avoid the incoming node
    while True:
      try:
        link_next.remove(prev_node)
      except ValueError:
        break
      #end_try
    #end_while

    prev_node = next_node
    next_node = random.choice(link_next)

    while prev_node == next_node:
      next_node = random.choice(link_next)
    #end_while

    path.append(next_node)
    count += 1
    print count 
  #end_while
  if count == 128:
    return None
  #end_if
  return path
#end_def



def cluster_coefficient(nodes):
  c_i = 0
  for i in nodes.itervalues():
    e_i = 0
    link = i.link
    for j in link:
      link_next = j.link
      for k in link_next:
        link_next_next = k.link
        for l in link_next_next:
          if l == i:
            #print "[",i.id,",",j.id,",",k.id,"]"
            e_i += 1
          #end_if
      #end_for
    #end_for

    #avoid the repetition of the same cluster
    try:
      e_i_avoid = float(e_i / 2)
      c_i += (2*e_i_avoid)/(len(link)*(len(link)-1))
    except ZeroDivisionError:
      pass
  #end_for
  cluster_coefficient = c_i / len(nodes)
  return cluster_coefficient
#end_def

def cluster_coefficient_per_node(nodes):
  c_i  = 0
  c_i_list = []
  for i in nodes.itervalues():
    print "start : ", i.id
    e_i = 0
    link = i.link
    for j in link:
      link_next = j.link
      for k in link_next:
        link_next_next = k.link
        for l in link_next_next:
          if l == i:
            #print "[",i.id,",",j.id,",",k.id,"]"
            e_i += 1
          #end_if
      #end_for
    #end_for

    #avoid the repetition of the same cluster
    try:
      e_i_avoid = float(e_i / 2)
      c_i = (2*e_i_avoid)/(len(link)*(len(link)-1))
      c_i_list.append(c_i)
    except ZeroDivisionError:
      c_i_list.append(0)
  #end_for
  return c_i_list
#end_def

def dijkstra(nodes, src_node, dst_node=None):

  if dst_node != None:
    if src_node == dst_node:
      return 0
    #end_if
  #end_if
  
  done = {}
  cost = 0
  done[src_node.id] = cost

  list = src_node.link
  #print "first-list", list
  while list != []: 
    cost += 1
    next = list
    list = []
    for i in next:
      if i.id in done:
        continue
      else:
        done[i.id] = cost
        list += i.link
        if dst_node != None:
          if i == dst_node:
            return cost
          #end_if
        #end_if
      #end_if
    #end_for
    #print "next-list", list
  #end_while
  #print done
  max_cost = cost -1
  return max_cost
#end_def


def list2file(file, list):
  fp = open(file, 'w')
  count = 0
  for i in list:
    s=str(count)
    s+=" "
    s+=str(i)
    s+="\n"
    fp.write(s)
    count += 1
  fp.flush()
  fp.close()
#end_def


def top2obj(filename):
  nodes = {}
  fp = open(filename, 'r')
  for i in fp:
    data=i.split()
    for j in data:
      if False == nodes.has_key(j):
        nodes[j] = node(j)
  fp.seek(0)
  for i in fp:
    data=i.split()
    nodes[data[0]].link.append(nodes[data[1]])
  return nodes

def hash_degree(hash):
  max = 0
  for i in hash.itervalues():
    if max < len(i.link):
      max = len(i.link)
    #end_if
  #end_for
  degree_list = []
  for i in xrange(max+1):
    degree_list.append(0)
  #end_for
  for i in hash.itervalues():
    degree_list[len(i.link)] += 1
  #end_for
  return degree_list
#end_def


#degree check
def list_degree(list):
  max = 0
  for i in list:
    if max < len(i.link):
      max = len(i.link)
    #end_if
  #end_for
  degree_list = []
  for i in xrange(max+1):
    degree_list.append(0)
  #end_for

  #print "print : ", degree_list

  for i in list:
    degree_list[len(i.link)] += 1
  #end_for
  return degree_list
#end_def

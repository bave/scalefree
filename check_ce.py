#!/usr/bin/env python
import sys
import utils

filename=sys.argv[1]
nodes=utils.top2obj(filename)

ce_list = utils.cluster_coefficient_per_node(nodes)
ce_list_sum = 0
for i in ce_list:
    ce_list_sum += i
ce = ce_list_sum / len(ce_list)

fp=open(filename+".ce",'w')
s=str(ce)
s+="\n"
fp.write(s)
fp.flush()
fp.close()

fp1=open(filename+".ce_list",'w')
fp2=open(filename+".ce_list_not_zero",'w')
for i in ce_list:
    s=""
    s+=str(i)
    s+="\n"
    fp1.write(s)
    if i != 0.0:
        fp2.write(s)
    #end_if
#end_if
fp1.flush()
fp1.close()
fp2.flush()
fp2.close()

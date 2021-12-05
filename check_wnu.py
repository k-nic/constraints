#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

def list_triples(n):
    triples = np.array([])
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i!=j and i!=k and j!=k:
                    np.append(triples, [i,j,k])
    return triples

def list_pairs(n):
    pairs = np.array([])
    for i in range(n):
        for j in range(n):
            if i!=j:
                np.append(pairs,[i,j])
    return pairs


# In[2]:


def cardinality(n):
    return n**(n*(n-1)*(n-2)+n*(n-1))
print(cardinality(2))


# In[ ]:


n=3

triples = list_triples(n)
pairs = list_pairs(n)

def digit_to_op(dig):
    op = np.zeros((n,n,n))
    for i in range(n):
        op[i][i][i] = i
    for pair in pairs[::-1]:
        print([pair[0],pair[1]])
        op[pair[0]][pair[1]][pair[1]] = dig % n
        op[pair[1]][pair[0]][pair[1]] = dig % n
        op[pair[1]][pair[1]][pair[0]] = dig % n
        dig = dig//n
    for triple in triples[::-1]:
        op[triple[0]][triple[1]][triple[2]] = dig % n
        dig = dig//n
    return op

def op_to_digit(op):
    dig=0
    for triple in triples:
        dig = dig*n + op[triple[0]][triple[1]][triple[2]]
    for pair in pairs:
        dig = dig*n + op[pair[0]][pair[1]][pair[1]]
    return dig

def superposition(o1,o2,o3,o4):
    o = np.zeros((n,n,n))
    for i in range(n):
        o[i][i][i] = i
    for triple in triples:
        o[triple[0]][triple[1]][triple[2]] = o1[o2[triple[0]][triple[1]][triple[2]]][o3[triple[0]][triple[1]][triple[2]]][o4[triple[0]][triple[1]][triple[2]]]
    for pair in pairs:
        o[pair[0]][pair[1]][pair[1]] = o1[o2[pair[0]][pair[1]][pair[1]]][o3[pair[0]][pair[1]][pair[1]]][o4[pair[0]][pair[1]][pair[1]]]
        o[pair[1]][pair[0]][pair[1]] = o1[o2[pair[1]][pair[0]][pair[1]]][o3[pair[1]][pair[0]][pair[1]]][o4[pair[1]][pair[0]][pair[1]]]
        o[pair[1]][pair[1]][pair[0]] = o1[o2[pair[1]][pair[1]][pair[0]]][o3[pair[1]][pair[1]][pair[0]]][o4[pair[1]][pair[1]][pair[0]]]
    return o

def compose(args):
    o1 = digit_to_op(args[0])
    o2 = digit_to_op(args[1])
    o3 = digit_to_op(args[2])
    o4 = digit_to_op(args[3])
    return op_to_digit(superposition(o1,o2,o3,o4))

def two(args):
    return compose([args[0],args[1],args[0],args[0]])

def fancy(args):
    return two([compose(args),compose([args[3],args[2],args[1],args[0]])])

c = cardinality(n)

for i in range(c):
    for j in range(c):
        if fancy([i,j,j,j])!=fancy([j,i,j,j]):
            print([i,j,j,j])
            print([j,i,j,j])
            print("Not really")
        if fancy([i,j,j,j])!=fancy([j,j,i,j]):
            print([i,j])
            print("Not really")
        if fancy([i,j,j,j])!=fancy([j,j,j,i]):
            print([i,j])
            print("Not really")


# In[ ]:


o = digit_to_op(0)


# In[ ]:


print("It finalizes")



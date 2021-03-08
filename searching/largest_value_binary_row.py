#Find the largest number of a row in a binary tree using Breadth First Search
#Just for fun!!
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def largestValuesInTreeRows(t):
    if not t:
        return []
    x,lev = [],[]
    r = []
    x.append([t,0]) #insert node with its level
    while len(x) > 0:
        nt,l = x.pop(0)
        if nt.value is not None:
            if not len(r): r.append([l,nt.value])
            elif r[len(r)-1][0]!=l: r.append([l,nt.value])
            elif r[len(r)-1][1]<nt.value:
                r.pop()
                r.append([l,nt.value])
        if nt.left is not None:
            x.append([nt.left,l+1])
        if nt.right is not None:
            x.append([nt.right,l+1])
    
    return [r[i][1] for i in range(len(r))]

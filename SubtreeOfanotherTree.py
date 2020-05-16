from typing import List
from PrintBTree import printBTree
from contextlib import suppress

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return printBTree(self,lambda n:(str(n.val),n.left,n.right))
      
####################### SOLUTION #################################################

def findHead(lis: List[TreeNode], s: TreeNode, t: TreeNode):
    if (s is None):
        return
    if(t.val == s.val):
        lis.append(s)
    findHead(lis, s.left, t)
    findHead(lis, s.right, t)
    
def isSame(s: TreeNode, t: TreeNode) -> TreeNode:
    if (s is None and t is None):
        return True
    if (s is None or t is None):
        return False
    if(s.val == t.val):
        return isSame(s.left, t.left) and isSame(s.right, t.right)
    else:
        return False
    
def isSubtree(s: TreeNode, t: TreeNode):
    lis = list()
    findHead(lis, s, t)
    for l in lis:
        if isSame(l,t):
            return True
    return False
    
##################################################################################


A = TreeNode(3)
A.left = TreeNode(4)
A.right = TreeNode(5)
A.left.left = TreeNode(1)
A.left.right = TreeNode(2)

B = TreeNode(4)
B.left = TreeNode(1)
B.right = TreeNode(2)    

print("\nInput: ")
print("A:")
with suppress(TypeError): print(A)
print("B:")
with suppress(TypeError): print(B)
print("Solution: ", isSubtree(A, B))

A.left.right.left = TreeNode(0)

print("\nInput: ")
print("A:")
with suppress(TypeError): print(A)
print("B:")
with suppress(TypeError): print(B)
print("Solution: ", isSubtree(A, B))

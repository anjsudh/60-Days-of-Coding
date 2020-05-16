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

def mergeTrees(t1: TreeNode, t2: TreeNode) -> TreeNode:
    if(t1 is None and t2 is None):
        return None
    if(t1 is None):
        return t2
    if(t2 is None):
        return t1
    else:
        node = TreeNode(t1.val + t2.val)
        node.left = mergeTrees(t1.left, t2.left)
        node.right = mergeTrees(t1.right, t2.right)
        return node

##################################################################################


A = TreeNode(1)
A.left = TreeNode(3)
A.right = TreeNode(2)
A.left.left = TreeNode(5)

B = TreeNode(2)
B.left = TreeNode(1)
B.right = TreeNode(3)
B.left.right = TreeNode(4)
B.right.right = TreeNode(7)    

print("\nInput: ")
print("A:")
with suppress(TypeError): print(A)
print("B:")
with suppress(TypeError): print(B)
print("Merged tree: ")
with suppress(TypeError): print(mergeTrees(A, B))

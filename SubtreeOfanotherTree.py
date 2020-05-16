from Tree import TreeNode
from typing import List

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
A.printTree()
print("B:")
B.printTree()
print("Solution: ", isSubtree(A, B))

A.left.right.left = TreeNode(0)

print("\nInput: ")
print("A:")
A.printTree()
print("B:")
B.printTree()
print("Solution: ", isSubtree(A, B))

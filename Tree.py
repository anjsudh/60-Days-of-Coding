from PrintBTree import printBTree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def printTree(self):
        printBTree(self,lambda n:(str(n.val),n.left,n.right))
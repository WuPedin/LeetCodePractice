"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node 
"""


class BSTIterator:
    """
    @param: root: The root of binary tree.
    """
    def __init__(self, root):
        self.stack = []
        self.findMostLeft(root)
            
    def findMostLeft(self, n):
        while n is not None:
            self.stack.append(n)
            n = n.left

    """
    @return: True if there has next node, or false
    """
    def hasNext(self):
        return len(self.stack) > 0

    """
    @return: return next node
    """
    def _next(self):
        node = self.stack.pop()
        
        if node.right:
            self.findMostLeft(node.right)

        return node 
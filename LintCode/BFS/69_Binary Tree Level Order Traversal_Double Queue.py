"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        
        res = []
        # Check 
        if not root:
            return res 
            
        # BFS, double queue
        q = [root]
        while q:
            next_q = []
            res.append([node.val for node in q])
            for node in q:
                if node.left: next_q.append(node.left)
                if node.right: next_q.append(node.right)
            q = next_q
            
        return res
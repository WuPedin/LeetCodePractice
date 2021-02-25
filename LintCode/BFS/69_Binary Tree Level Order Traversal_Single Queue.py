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
            
        # BFS
        q = collections.deque([root])
        while q:
            val_this_lvl = []
            for _ in range(len(q)):
                node = q.popleft()
                val_this_lvl.append(node.val)
                
                # Append children
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(val_this_lvl)
            
        return res
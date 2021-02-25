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
        
        # Check
        if not root:
            return []
            
        # BFS using dummy node 
        res, val_this_lvl = [], [] 
        q = collections.deque([root, None])
        while q:
            node = q.popleft()
            if node is None:
                res.append(val_this_lvl)
                val_this_lvl = []
                if q: q.append(None)
                continue
            
            val_this_lvl.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
                
        return res

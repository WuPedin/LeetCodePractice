"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        res = []
        
        # Check
        if not root:
            return res
        
        # Deque
        q = collections.deque([root])
        while q:
            val_this_lvl = []
            cnt_this_lvl = len(q)
            while cnt_this_lvl:
                node = q.popleft()
                val_this_lvl.append(node.val)
                for c in node.children:
                    q.append(c)
                cnt_this_lvl -= 1
            res.append(val_this_lvl)
        
        return res
        
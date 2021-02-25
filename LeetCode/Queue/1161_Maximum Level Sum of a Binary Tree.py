# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        
        # No need to check if not root, number of nodes in the tree is in the range [1, 104]
        
        lvl, res, res_lvl = 1, root.val, 1
        q = collections.deque([root])
        while q:
            cnt_this_lvl = len(q)
            sum_this_lvl = 0
            while cnt_this_lvl:
                node = q.popleft()
                sum_this_lvl += node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                cnt_this_lvl -= 1
            
            if sum_this_lvl > res:
                res = sum_this_lvl
                res_lvl = lvl
            lvl += 1
        
        return res_lvl
            
        
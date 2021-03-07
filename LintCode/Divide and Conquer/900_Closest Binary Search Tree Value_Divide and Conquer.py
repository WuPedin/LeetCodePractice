"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):

        lower_bound = float('-inf')
        upper_bound = float('inf')
        while root:
            if root.val == target:
                return root.val
            elif root.val < target:
                lower_bound = root.val
                root = root.right
            elif root.val > target:
                upper_bound = root.val
                root = root.left

        if upper_bound - target < target - lower_bound:
            return upper_bound
        else:
            return lower_bound

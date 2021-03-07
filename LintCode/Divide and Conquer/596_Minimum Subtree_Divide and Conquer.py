"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    """
    思路：
        使用建立函數TreeSum(root)以得到root的子樹的sum，用遞迴的方式得到整顆樹的sum
        順便打擂台，找sum最小的子樹
    """
    def findSubtree(self, root):
        minimun, subtree, sum_root = self.helper(root)
        return subtree

    def helper(self, root):

        if root is None:
            return sys.maxsize, None, 0

        # Get sum of root
        left_minimun, left_subtree, left_sum = self.helper(root.left)
        right_minimun, right_subtree, right_sum = self.helper(root.right)
        sum_root = left_sum + right_sum + root.val

        # Get min sum 
        if left_minimun == min(left_minimun, right_minimun, sum_root):
            return left_minimun, left_subtree, sum_root
        if right_minimun == min(left_minimun, right_minimun, sum_root):
            return right_minimun, right_subtree, sum_root

        return sum_root, root, sum_root




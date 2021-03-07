"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):
        self.flatten_and_return_last_node(root)
     
    # Reconstruct and return last node in preorder
    def flatten_and_return_last_node(self, root):
        if root is None:
            return None 

        left_last = self.flatten_and_return_last_node(root.left)
        right_last = self.flatten_and_return_last_node(root.right)

        # Connect
        if left_last is not None:
            left_last.right = root.right
            root.right = root.left
            root.left = None 

        return right_last or left_last or root"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        dummy = TreeNode(0)
        dummy.right = root
        stack = [dummy]

        # 如果有右子樹，就會往右子樹的最左邊一路走到底，沿路加入stack
        # 中序遍歷會由小到大被pop出來，第一個被pop的是dummy
        # 所以要找第k小的，可以pop k次，stack中最後一個數就是第k小的數
        for i in range(k):
            node = stack.pop()
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left

            if not stack:
                return None

        return stack[-1].val
            
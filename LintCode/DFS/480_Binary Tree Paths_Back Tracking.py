class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        
        # Check
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        
        return self.findPaths(root, [root], [])
        
        
    def findPaths(self, node, path, paths):
        if not node:
            return 
        # Leaf node 
        if not node.left and not node.right:
            paths.append('->'.join([str(n.val) for n in path]))
            return
        
        path.append(node.left)
        self.findPaths(node.left, path, paths)
        path.pop()
        
        path.append(node.right)
        self.findPaths(node.right, path, paths)
        path.pop()
        return paths
        
      
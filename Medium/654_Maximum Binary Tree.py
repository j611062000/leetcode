# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: 
        	return None

        elif not root.left and not root.right and not root.val:
        	return None

        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)

        if root.val:
        	return root

        elif root.left is None and root.right is None:
        	return None

        else:
        	return root


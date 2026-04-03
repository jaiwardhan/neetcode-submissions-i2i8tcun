# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def post_helper(root):
            if root is None:
                return
            post_helper(root.left)
            post_helper(root.right)
            root.left, root.right = root.right, root.left
        
        post_helper(root)
        return root
        


"""

Post order traversal : look both children then process the current node
when returning back from pot (bubble up phase) do compare and swap the linkages

"""
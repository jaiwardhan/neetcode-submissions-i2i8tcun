# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def post_helper(root):
            if root is None:
                return 0
            return max(post_helper(root.left), post_helper(root.right))+1
        
        return post_helper(root)


"""
post order traversal:
When returning back from pot (bubbling up phase): return +1 counting the node
when processing on the node after children, take max from children and add 1 and send

"""
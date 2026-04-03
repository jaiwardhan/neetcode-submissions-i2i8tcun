# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def post_helper(a, b):
            if a is None and b is None:
                return True
            if a is None or b is None:
                return False
            
            return post_helper(a.left, b.left) and post_helper(a.right, b.right) and a.val == b.val
        
        return post_helper(p, q)


"""
use post order traversal:
during bubbling up phase, compare structure and values, return true|False
when processing in parent, check if any is false from below (use AND) and send upwards

"""
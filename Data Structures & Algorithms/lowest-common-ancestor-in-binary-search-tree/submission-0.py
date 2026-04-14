# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def trace_path(ref_node, curr_node):
            if curr_node.val == ref_node.val:
                return [curr_node]

            return [curr_node] + \
                ( trace_path(ref_node, curr_node.left) if curr_node.val > ref_node.val else trace_path(ref_node, curr_node.right))
        
        tp1 = trace_path(p, root)
        tp2 = trace_path(q, root)
        if len(tp1) == 0 or len(tp2) == 0:
            return None
        anc = tp1[0]
        i = 1
        while i < len(tp1) and i < len(tp2):
            if tp1[i].val != tp2[i].val:
                break
            anc = tp1[i]
            i += 1
        
        return anc


"""
- Trace path to the p node [s1,s2,...,p]
- Trace path to the q node [s1,s2....,q]
start from i = 0
-> till tp1[i] == tp2[i]

where i points is the lowest common ancestor

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        op = []
        if root is None:
            return op
        op.append([])
        dq = deque([root, "n"])
        while len(dq) > 0:
            elem = dq.popleft()
            if type(elem) is TreeNode:
                op[-1].append(elem.val)
                if elem.left is not None:
                    dq.append(elem.left)
                if elem.right is not None:
                    dq.append(elem.right)
                continue
            
            # This is a delimiter string
            # If we still have more nodes to process, there is potentially more
            # levels to add, hence only re-add this delimiter if there is more
            # work to do, else we are good to skip
            if len(dq) > 0:
                dq.append(elem)
                op.append([])
        return op

"""
Level order is primarily done using stack
-> But how do we know where to parition?
    -> INtroduce a level delimiter

1-n
n-2-3
2-3-n
3-n-4-5
n-4-5-6-7
4-5-6-7-n
...
n (If len of stack is 0 i.e. nothing more -- break)

When encounter n:
add a blank [] at end of the list
Every node gets appened to [-1].append()

// Spc -> < O(n)
// time -> O(n)

"""
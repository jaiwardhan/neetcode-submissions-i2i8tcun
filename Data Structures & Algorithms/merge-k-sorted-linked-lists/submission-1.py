# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        root = None
        e_root = None
        lookup = {}
        k = len(lists)

        def populate_lookup(lists):
            for i in range(len(lists)):
                lookup[i] = lists[i]

        def get_least_index():
            l_node_index = -1
            for i in range(k):
                if l_node_index == -1:
                    if lookup[i] is not None:
                        l_node_index = i
                    continue
                
                if lookup[i] is None:
                    continue

                l_node_index = l_node_index if lookup[l_node_index].val < lookup[i].val else i
            
            return l_node_index
        
        def move_next(index):
            if lookup[index] is None:
                return

            lookup[index] = lookup[index].next

        populate_lookup(lists)
        while True:
            idx = get_least_index()
            if idx == -1:
                break
            
            if root is None:
                root = lookup[idx]
                e_root = root
            else:
                e_root.next = lookup[idx]
                e_root = e_root.next
            move_next(idx)

        return root



"""
Each LL can have a different length.

Alg:
- Iterate throguh k LLs. Each LL has a current pointer
    - Find the pointer for the least element 
    - move it to next

- How do you start with the minimum pointer
- What do you do when you reach the EOL

{
    0: cp0* 
    1: cp1*
    2: cp2*
}

On moving next if the next is None: mark in the index correspoding as NONE
On starting the iter loop, skim through till we find a non NONE index.
 ==> If you find none, all are done, and break


def get_least_index() -> -1 if found none, else the index to the next least element
def move_next(index) -> moves the pointer for this index to next and sets NONE if EOLL

"""
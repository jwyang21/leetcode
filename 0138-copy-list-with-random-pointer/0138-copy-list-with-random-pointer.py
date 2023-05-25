# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

# https://github.com/kamyu104/LeetCode-Solutions/blob/master/Python/copy-list-with-random-pointer.py
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # copy and combine the copied list with original list.
        current = head
        while current:
            copied = Node(current.val)
            copied.next = current.next
            current.next = copied
            current = copied.next
            
        # update random node in copied list
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next
        
        # split copied list from combined one
        dummy = Node(0)
        copied_current, current = dummy, head
        while current:
            copied_current.next = current.next
            current.next = current.next.next
            copied_current, current = copied_current.next, current.next
        return dummy.next
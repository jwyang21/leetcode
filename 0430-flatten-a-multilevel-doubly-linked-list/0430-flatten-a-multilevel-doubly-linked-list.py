"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
#https://walkccc.me/LeetCode/problems/0430/
class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        while curr is not None:
            if curr.child is not None:
                cachedNext = curr.next
                curr.next = curr.child
                curr.child.prev = curr
                curr.child = None
                tail = curr.next
                while tail.next is not None:
                    tail = tail.next
                tail.next = cachedNext
                if cachedNext is not None:
                    cachedNext.prev = tail
            curr = curr.next
        return head
        
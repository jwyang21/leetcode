# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#https://leetcode.com/problems/rotate-list/solutions/458710/rotate-list-in-python/
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Given the head of a linked list, rotate the list to the right by k places.
        p =head
        n = 1
        if(head is None):
            return head
        if(p.next is None):
            return head
        if(p.next.next is None):
            if(k%2 == 0):
                return head
            else:
                p.next.next = head
                head = p.next
                p.next = None
            return head
        while(p.next):
            n += 1
            p = p.next
        else:
            p = head
            if(k>n):
                k %= n
            while (k>0):
                if(p.next.next is None):
                    p.next.next = head
                    head = p.next
                    p.next = None
                    p = head
                    k -= 1
                p = p.next
            return head
        
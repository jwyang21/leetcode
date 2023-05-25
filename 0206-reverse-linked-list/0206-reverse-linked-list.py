# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        else:
            val_list = []
            curr = head
            while curr.next is not None:
                val_list.append(curr.val)
                curr = curr.next
            val_list.append(curr.val)
            
            h = ListNode(val_list[-1])
            curr = h
            for i in range(1, len(val_list)):
                curr.next = ListNode(val_list[len(val_list)-1-i])
                curr = curr.next
            return h
        
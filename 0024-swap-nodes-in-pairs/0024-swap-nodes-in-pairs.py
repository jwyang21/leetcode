# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        else:
            val_list = []
            curr = head
            while curr.next is not None:
                val_list.append(curr.val)
                curr = curr.next
            val_list.append(curr.val) #next value of the last node is None
            
            tmp = 0
            while tmp < len(val_list)-1:
                val_list[tmp], val_list[tmp+1] = val_list[tmp+1], val_list[tmp]
                tmp += 2
            
            h = ListNode(val_list[0])
            curr = h
            for i in range(len(val_list)-1):
                curr.next = ListNode(val_list[i+1])
                curr = curr.next
            return h
                
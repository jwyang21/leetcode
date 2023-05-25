# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        val_list = []
        # 전체 node들을 순방향으로 traverse하면서 value들을 순차적으로 저장. 
        while head != None:
            val = head.val
            val_list.append(val)
            head = head.next
        if val_list == val_list[::-1]:
            return True
        else:
            return False
            
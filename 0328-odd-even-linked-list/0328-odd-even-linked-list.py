# return (odd index nodes + even index nodes)

# definition for singly linked list
class ListNode():
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
        
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # 리스트로 바꿔서 리스트 인덱스 짝수인거를 뺴서 뒤로 넣기
        node = head
        even = []
        odd = []
        lists = []
        answers = []

        while node is not None :
            lists.append(node.val)
            node = node.next

        for i, x in enumerate(lists) :
            if i % 2 == 1 :
                even.append(x)
            else :
                odd.append(x)
        answers = odd + even

        prev = None
        while answers :
            node = ListNode(answers.pop())
            node.next = prev
            prev = node

        return node

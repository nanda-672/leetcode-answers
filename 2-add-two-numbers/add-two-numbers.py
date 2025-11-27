# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertTail(self, head: Optional[ListNode], val: int) ->  Optional[ListNode]:

        if head is None:
            return ListNode(val)
        
        last = head
        while last.next:
            last = last.next
        
        last.next = ListNode(val)

        return head


    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        num2 = 0

        if l1.val == 0 and l1.next == None:
            return l2
        if l2.val == 0 and l2.next == None:
            return l1

        answer_node = ListNode((l1.val + l2.val)%10)
        carry = (l1.val + l2.val)//10
        while True:
            if l1.next and l2.next:
                l1 = l1.next
                l2 = l2.next
                answer_node = self.insertTail(answer_node, (l1.val + l2.val + carry)%10)
                carry = (l1.val + l2.val + carry)//10
            elif l1.next:
                l1 = l1.next
                answer_node = self.insertTail(answer_node, (l1.val + carry)%10)
                carry = (l1.val + carry)//10
            elif l2.next:
                l2 = l2.next
                answer_node = self.insertTail(answer_node, (l2.val + carry)%10)
                carry = (l2.val + carry)//10
            elif carry != 0:
                answer_node = self.insertTail(answer_node, carry)
                carry = 0
            else:
                break            
        return answer_node
        
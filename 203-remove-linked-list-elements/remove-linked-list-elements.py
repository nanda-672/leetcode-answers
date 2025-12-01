# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy

        while head:
            print(head.val)
            if head.val != val:
                cur.next = head
                cur = head
                head = head.next
            else:
                head = head.next
                cur.next = head
        return dummy.next
        
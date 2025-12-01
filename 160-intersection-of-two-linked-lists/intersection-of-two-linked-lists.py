# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        memo = {}
        cur_a = headA
        while cur_a:
            memo[cur_a] = cur_a.val
            cur_a = cur_a.next
        cur_b = headB
        while cur_b:
            if cur_b in memo:
                return cur_b
            cur_b = cur_b.next
        return None
        
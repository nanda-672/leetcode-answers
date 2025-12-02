# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next == None:
            return True

        cur = head
        stack_arr = [cur.val]
        cur = cur.next

        while cur:
            # if cur.val == stack_arr[-1]:
            #     stack_arr.pop()
            # else:
            #     stack_arr.append(cur.val)
            stack_arr.append(cur.val)
            
            cur = cur.next
        
        # print(stack_arr)
        # if len(stack_arr):
        #     return False
        # else:
        #     return True

        if stack_arr == stack_arr[::-1]:
            return True
        else:
            return False
                        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = 0
        i=0
        while l1 is not None:
            n1 += l1.val * 10 ** i
            l1 = l1.next
            i+=1
            
        n2 = 0
        i=0
        while l2 is not None:
            n2 += l2.val * 10 ** i
            l2 = l2.next
            i+=1
            
        num = n1 + n2
        
        output = ListNode()
        builder = output
        
        while num//10 != 0:
            
            builder.val = num%10
            num = num//10
            builder.next = ListNode()
            builder = builder.next
        
        builder.val = num%10
        
        return output

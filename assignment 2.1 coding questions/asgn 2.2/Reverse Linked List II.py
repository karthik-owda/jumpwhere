# Reverse Linked List II
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode(-1,head)
        left_prev,curr=dummy,head
        for i in range(left-1):
            left_prev,curr=curr,curr.next
        prev=None
        for i in range(right-left+1):
            next_ptr=curr.next
            curr.next=prev
            prev,curr=curr,next_ptr
        left_prev.next.next=curr
        left_prev.next=prev
        return dummy.next

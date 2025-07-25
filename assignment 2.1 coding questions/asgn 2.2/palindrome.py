class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast,slow=head,head
        while (fast) and (fast.next):
            fast=fast.next.next
            slow=slow.next
        
        prev=None
        while slow!=None:
            n_ptr=slow.next
            slow.next=prev
            prev=slow
            slow=n_ptr
        
        left=head
        right=prev
        while right!=None:
            if left.val!=right.val:
                return False
            left=left.next
            right=right.next
        return True

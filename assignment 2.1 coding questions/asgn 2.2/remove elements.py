# Remove Linked List Elements
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        while head.val==val:
            if head.next:
                head=head.next
            else:
                head=None
                return head
        curr=head.next
        prev=head
        while curr!=None:
            if curr.val==val:
                if curr.next==None:
                    prev.next=None
                prev.next=curr.next
                curr=curr.next
                continue
            curr=curr.next
            prev=prev.next
        return head

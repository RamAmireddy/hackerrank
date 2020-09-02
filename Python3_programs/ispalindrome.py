
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome( head):
    """
    :type head: ListNode
    :rtype: bool
    """

    def reverse(head):
        if head.next is None:
            return head
        tmp = head
        tmp2 = reverse(tmp.next)
        tmp.next.next = tmp
        tmp.next = None
        return tmp2

    s = head
    f = head
    while f is not None and f.next is not None and f.next.next is not None:
        s = s.next
        f = f.next.next
    f = s.next
    f = reverse(f)
    while s and f:
        if s.val != f.val:
            return False
        s = s.next
        f = f.next
    return True
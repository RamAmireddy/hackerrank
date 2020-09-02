
def mergeTwoLists( l1, l2):
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    head = l1 if l1.val < l2.val else l2
    prev=None

    while (l1 and l2):
        if (l1.val < l2.val):
            if l1.next is not None and l1.next.val < l2.val:
                prev=l1
                l1 = l1.next
            else:
                tmp = l1.next
                l1.next = l2
                l2 = tmp
                prev=l2
                l1 = l1.next
        else:
            if l2.next is not None and l2.next.val < l1.val:
                prev=l2
                l2 = l2.next
            else:
                tmp = l2.next
                l2.next = l1
                l1 = tmp
                prev=l1
                l2 = l2.next

    if prev is not None and l1 is None:
        prev.next=l2
    elif prev is not None:
        prev.next=l1

    return head
def createll(ar):
    head = ListNode()
    head.val = ar[0]
    tmp = head
    for i in range(1,len(ar)):
        t = ListNode()
        t.val = ar[i]
        tmp.next = t
        tmp = tmp.next
    return head

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
l1=createll([-2,5])
l2=createll([-9,-6,-3,-1,1,6])

ls=mergeTwoLists(l1,l2)
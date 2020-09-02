def reorderList(head):
    """
    :type head: ListNode
    :rtype: None Do not return anything, modify head in-place instead.
    """
    def reverse(l):
        if l is None: return None

        cur = l
        prev = None
        nxt = None

        while cur is not None:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev
    s=head
    f=head
    while f is not None and f.next is not None:
        s=s.next
        f=f.next.next
    h1=head
    head2=s.next
    s.next=None
    h2=reverse(head2)

    print(h1,h2)

    while h2 is not None:
        tmp=h1.next
        h1.next=h2
        h2=h2.next
        h1.next.next=tmp
        h1=h1.next.next

    return head


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


ar=[2,3,4]

head = ListNode()
head.val=1
tmp=head
for i in ar:
    t= ListNode()
    t.val=i
    tmp.next=t
    tmp=tmp.next
h = reorderList(head)
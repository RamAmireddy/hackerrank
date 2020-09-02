class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def revkgroup(head, k):
    cnt = 1
    tmp = head
    while cnt < k and tmp.next != None:
        cnt += 1
        tmp = tmp.next
    nextk = tmp.next
    head = Solution.reverse(head)
    nextk = Solution.revkgroup(nextk, k)
    tmp = head
    while tmp.next != None:
        tmp = tmp.next
    tmp.next = nextk
    return head

def reverseKGroup( head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """

    def reverse(head):
        prev = None
        current = head
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev

    def revkgroup(head, k):
        if head == None:
            return None
        cnt = 1
        tmp = head
        while cnt < k and tmp.next != None:
            cnt += 1
            tmp = tmp.next
        nextk = tmp.next
        tmp.next=None
        head = reverse(head)
        nextk = revkgroup(nextk, k)
        tmp = head
        while tmp.next != None:
            tmp = tmp.next
        tmp.next = nextk
        return head

    #         cnt=1
    #         tmp=head
    #         while cnt<k and tmp.next!=None:
    #             cnt+=1
    #             tmp = tmp.next
    #         nextk = tmp.next
    #         head = Solution.reverse(head)
    #         nextk = Solution().reverseKGroup(nextk,k)

    #         tmp = head
    #         while tmp.next!=None:
    #             tmp=tmp.next
    #         tmp.next=nextk

    return revkgroup(head, k)


ar=[3,2,4,5]

head = ListNode()
head.val=1
tmp=head
for i in ar:
    t= ListNode()
    t.val=i
    tmp.next=t
    tmp=tmp.next

head  = reverseKGroup(head,3)

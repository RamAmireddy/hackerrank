class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
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

n,k=5,3
nums=[1,-1,0,1,-1]
head=createll(nums)
cnt=0
s=head
flag=0
k=n-k
print(k)
cnt=1
s=head
while cnt < k:
    cnt+=1
    s=s.next
tmp = s.next.next
s.next=tmp
tmp=head
while tmp is not None:
    print(tmp.val,)
    tmp=tmp.next


# https://www.hackerrank.com/challenges/jesse-and-cookies/problem






import heapq
def cookies(k, A):
    #
    # Write your code here.
    #
    heapq.heapify(A)
    op=0
    s=0

    while s<k and len(A)>=2:
        op+=1
        x=heapq.heappop(A)
        y=heapq.heappop(A)
        s=x+2*y
        print(s)
        heapq.heappush(A,s)
    if s>=k:
        return op


k=7
A = list(map(int,"1 2 3 9 10 12".split(" ")))
print(cookies(7,A))
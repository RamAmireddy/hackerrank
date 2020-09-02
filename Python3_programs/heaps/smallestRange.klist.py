

import heapq

class Pair():

    def __init__(self,val,i,j):
        self.val = val
        self.i = i
        self.j = j

    def __lt__(self, other):

        return self.val < other.val



def smallestRange(numbers):
    # code here
    # print the smallest range in a new line
    ls = []
    mx = numbers[0][0]
    for i in range(len(numbers)):
        mx = max(mx,numbers[i][0])
        ls.append(Pair(numbers[i][0],i,0))
    heapq.heapify(ls)
    mn = ls[0].val
    ans = [mn,mx]
    while 1:
        x= heapq.heappop(ls)

        if ans[1]-ans[0] > mx - x.val:
            ans = [x.val,mx]
        if x.j+1 >= len(numbers[0]) :
            break

        heapq.heappush(ls,Pair(numbers[x.i][x.j+1],x.i,x.j+1))
        mx = max(mx,numbers[x.i][x.j+1])

    print(*ans)



numbers =[
[1,3,5,7,9],
[0,2,4,6,8],
[2,3,5,7,11]]


numbers = [[1,2,3,4],
[5,6,7,8],
[9,10,11,12]]
smallestRange(numbers)
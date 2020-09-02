# https://leetcode.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/

import heapq

class Pair():

    def __init__(self,val,i,j):
        self.val = val
        self.i = i
        self.j = j

    def __lt__(self, other):

        return self.val < other.val

def kthsmallestsum(mat,K):

    ls=[]
    s = 0
    for i in range(len(mat)):
        ls.append(Pair(mat[i][0],i,0))
        s+=mat[i][0]
    heapq.heapify(ls)
    flag = 0
    while K:
        K = K-1
        x = heapq.heappop(ls)
        print(s)

        if x.j + 1 >= len(mat[0]):
            flag=1
            break

        heapq.heappush(ls, Pair(mat[x.i][x.j + 1], x.i, x.j + 1))
        s = s+mat[x.i][x.j + 1]
        s = s-x.val


    return s


mat = [[1,10,10],[1,4,5],[2,3,6]]
k = 7

print(kthsmallestsum(mat,k))


import math

def populate(arr, sq):
    n = len(arr)
    minarr = []
    nblks = int(n/sq)
    nblks += 1 if nblks*sq < n else 0
    for i in range(nblks):
        mn = float('inf')
        for j in range(sq):
            mn = min(arr[min(i * sq + j,n-1)], mn)

        minarr.append(mn)


    return minarr


def find(i, j, minarr, sq, arr):
    iblk = int(i / sq)
    strt = i % sq
    jblk = int(j / sq)
    endblk = j % sq
    mnstblk = float('inf')
    mnedblk = float('inf')
    mn = float('inf')
    stblk = iblk
    if strt > 0:
        stblk = iblk + 1
        for k in range(iblk * sq + strt, min((iblk + 1) * sq,j+1)):
            mnstblk = min(mnstblk, arr[k])

    for i in range(stblk, jblk):
        mn = min(mn, minarr[i])

    if endblk == sq - 1 and iblk!=jblk:
        mnedblk = minarr[int(jblk)]
    else:

        for k in range(max(i,jblk * sq), j+1):
            mnedblk = min(mnedblk, arr[k])

    return min([mnstblk, mn, mnedblk])
#
# 3
# 1 4 1
# 2
# 1 1
# 1 2
#
# n = 9
# arr = [2,3,4,5,6,3,1,3,2]
# sq = int(math.sqrt(n))
# mat = populate(arr, sq)
# q = [[0,0]]
# for i, j in q:
#     # i, j = map(int, input().strip().split(' '))
#     print(find(i, j, mat, sq, arr))
#
n = int(input().strip())
arr = list(map(int,input().strip().split(' ')))
sq = int(math.sqrt(n))
mat = populate(arr,sq)
q = int(input().strip())
while q:
    i,j = map(int,input().strip().split(' '))
    print(find(i,j,mat,sq,arr))
    q-=1
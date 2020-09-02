import heapq

def get_kthsmallest(matrix,k):
    if matrix is None or k <= 0:
        return 0
    ls = [[matrix[0][0], 0, 0]]
    mp = set((0, 0))
    ans = 0
    while k:
        k = k - 1
        ans, i, j = heapq.heappop(ls)
        if i + 1 < len(matrix) and (i + 1, j) not in mp:
            heapq.heappush(ls, [matrix[i+1][j],i+1,j])
            mp.add((i+1,j))

        if j+1 < len(matrix) and (i , j+1) not in mp:
            heapq.heappush(ls, [matrix[i][j+1],i,j+1])
            mp.add((i, j+1))

    return ans


matrix =[
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 9
print(get_kthsmallest(matrix,k))
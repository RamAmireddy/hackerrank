import heapq
def merge(numbers):
    # code here
    # return merged list
    ans = []
    ls = []
    for i in range(0,len(numbers)):
        ls.append([numbers[i][0],i,0])
    heapq.heapify(ls)
    while(len(ls)):
        x,i,j = heapq.heappop(ls)
        ans.append(x)
        if j+1<len(numbers):
            heapq.heappush(ls,[numbers[i][j+1],i,j+1])

    return ans




numbers = [[1, 2, 3],

             [4, 5, 6],

             [7, 8, 9]]
# numbers = [[1, 2, 2, 2],
#
#              [3, 3, 4, 4],
#
#              [5, 5, 6, 6],
#
#              [7, 8, 9, 9 ]]

print(merge(numbers))
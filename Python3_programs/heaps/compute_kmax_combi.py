import heapq
def compute_kmax_combi(arr1,arr2,k):
    ls = []
    i=len(arr1)-1
    j=len(arr2)-1
    ls.append([-1 *(arr1[i]+arr2[j]),i,j])
    ans=[]
    mp = set()
    mp.add((i,j))
    while k:
        k=k-1
        x,i,j = heapq.heappop(ls)
        ans.append(-1*x)
        if j-1>=0 and (i,j-1) not in mp:
            heapq.heappush(ls,[-1 * (arr1[i]+arr2[j-1]),i,j-1])
            mp.add((i,j-1))
        if i-1 >=0 and (i-1,j) not in mp:
            heapq.heappush(ls,[-1 * (arr1[i-1]+arr2[j]),i-1,j])
            mp.add((i-1,j))

    return ans



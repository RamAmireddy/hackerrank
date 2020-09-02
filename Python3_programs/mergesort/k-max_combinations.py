"""Given two equally sized arrays (A, B) and N (size of both arrays).
A sum combination is made by adding one element from array A and another element of array B. Display the maximum K valid sum combinations from all the possible sum combinations.

Examples:

Input :  A[] : {3, 2}
         B[] : {1, 4}
         K : 2 [Number of maximum sum
               combinations to be printed]
Output : 7    // (A : 3) + (B : 4)
         6    // (A : 2) + (B : 4)"""

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



a = [4, 2, 5, 1]
b = [8, 0, 3, 5]
ans = compute_kmax_combi(sorted(a),sorted(b),3)
print(ans)
# https://leetcode.com/problems/maximum-performance-of-a-team/
"""There are n engineers numbered from 1 to n and two arrays: speed and efficiency, where speed[i] and efficiency[i] represent the speed and efficiency for the i-th engineer respectively. Return the maximum performance of a team composed of at most k engineers, since the answer can be a huge number, return this modulo 10^9 + 7.

The performance of a team is the sum of their engineers' speeds multiplied by the minimum efficiency among their engineers.



Example 1:

Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
Output: 60"""
import heapq

List = list
class Pair():
    def __init__(self,s,e):
        self.s = s
        self.e = e
    def __lt__(self, other):
        if self.e>other.e:
            return True
        elif self.e<other.e:
            return False
        else:
            return self.s>other.e
def maxPerformance( n, speed, efficiency, k):

    ls = []

    for i in range(n):
        ls.append([speed[i],efficiency[i]])

    ls.sort(key=lambda x:[x[1],x[0]],reverse=True)
    # for i in range(n):
    #     print(ls[i][0],ls[i][1])

    hp = [ls[0]]
    ans  = ls[0][0]*ls[0][1]

    s = ls[0][0]
    mn = ls[0][1]
    for i in range(1,k):
        heapq.heappush(hp,ls[i])
        s = s + ls[i][0]
        mn = min(mn,ls[i][1])
        ans = max(ans,s*mn)

    for i in range(k,n):
        top = hp[0]
        if top[0] < ls[i][0] or( top[0] == ls[i][0] and top[1] < ls[i][1]):
            heapq.heappop(hp)
            heapq.heappush(hp,ls[i])
            s=s-top[0]+ls[i][0]
            mn = min([i[1] for i in hp])
            ans = max(ans,s*mn)


    print(ans)




n = 6
speed = [2,10,3,1,5,8]
efficiency = [5,4,3,9,7,2]
k = 2


n = 6
speed = [2,10,3,1,5,8]
efficiency = [5,4,3,9,7,2]
k = 3
maxPerformance(n,speed,efficiency,k)
# 1 9
# 2 5
# 3 3
# 5 7
# 8 2
# 10 4
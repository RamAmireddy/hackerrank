import math


def count_max_no_cuts(n,x,y,z):

    dp = [-1 for i in range(n+1)]

    def count_cuts(n,x,y,z):
        nonlocal dp
        if n==0: return 0
        if n<0: return -math.inf

        if dp[n] != -1: return dp[n]
        dp[n]= 1 + max( count_cuts(n-x,x,y,z),count_cuts(n-y,x,y,z),count_cuts(n-z,x,y,z))

        return dp[n]

    return count_cuts(n,x,y,z)


def count_max_no_cuts2(n, x, y, z):   #bottom-top method
    dp = [-1 for i in range(n + 1)]
    dp[0] = 0

    for i in range(1, n + 1):

        if i - x >= 0 and dp[i - x] >= 0 :
            dp[i] =  max(dp[i],1 + dp[i - x])
        if i - y >= 0 and dp[i - y] >= 0:
            dp[i] = max(dp[i],1 + dp[i - y])
        if i - z >= 0 and dp[i - z] >= 0:
            dp[i] = max(dp[i], 1 + dp[i - z])


    return dp[n]
#
# 4000
# 1 1 1



if __name__ == "__main__":
    import sys
    print(sys.getrecursionlimit())
    print(sys.setrecursionlimit(4005))

    # t = int(input().strip())
    #
    # while t:
    #     t=t-1
    #     n = int(input().strip())
    #     x,y,z = map(int,input().strip().split(" "))
    #
    #     ans = count_max_no_cuts2(n,x,y,z)
    #
    #     print(ans)
    #
    #
    #     ex:





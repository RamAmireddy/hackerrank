# https://leetcode.com/problems/distant-barcodes/

import heapq

class Pair():

    def __init__(self,num,freq):

        self.num=num
        self.freq=freq


    def __lt__(self, other):

        return self.freq > other.freq


    def __repr__(self):
        return str([self.num,self.freq])


def rearrangeBarcodes(barcodes):

    mp = {}

    for i in barcodes:
        if i in mp.keys():
            mp[i] = mp[i]+1
        else:
            mp[i]=1

    codesq=[]
    for key,freq in mp.items():
        codesq.append(Pair(key,freq))
    heapq.heapify(codesq)
    print(codesq)
    ans = []
    while len(codesq)>0:

        cycle = []
        i=0
        while i<2:
            x = heapq.heappop(codesq)
            ans.append(x.num)
            if x.freq-1>0:
                x.freq -= 1
                cycle.append(x)
            i=i+1
        for p in cycle:
            heapq.heappush(codesq,p)


    print(ans)
bars = [1,1,1,1,2,2,3,3]
rearrangeBarcodes(bars)
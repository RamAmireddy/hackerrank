# We have a list of points on the plane.  Find the K closest points to the origin
# (Here, the distance between two points on a plane is the Euclidean distance.)
#
# You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

import heapq

class point():
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __lt__(self, other):

        d1 = self.x*self.x + self.y*self.y
        d2 = other.x*other.x + other.y*other.y

        return d1<d2
    def __repr__(self):

        return str([",".join([str(self.x), str(self.y)])])

class Solution:

    def kClosest(self, points, k):
        pts = []
        ans = []
        for i in points:
            pt = point(i[0],i[1])
            pts.append(pt)

        heapq.heapify(pts)
        print(pts)
        while k:
            k=k-1
            ans.append(heapq.heappop(pts))

        return ans




s = Solution()
pts = s.kClosest([[3,3],[5,-1],[-2,4]],2)              #[[-2, 2], [1, 3]],1)
print(pts)


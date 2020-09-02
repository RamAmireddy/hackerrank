'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
class NumArray():

    def __init__(self, nums):

        self.nums = nums
        self.segtree = [[0,0]]*(4*len(nums))
        if len(nums):
            self.generate_seg_tree(0,len(nums)-1,1)
        # print(self.segtree)




    def update(self, i, val):
        self.upate_seg_tree(i-1,val,0,len(self.nums)-1,1)
        # print(self.segtree)


    def countRange(self,t, i, j):

       print(self.get_oddeven_count(i,j,0,len(self.nums)-1,1)[t-1])

        #. MY methods
        # [evencount,oddcount]

    def generate_seg_tree(self,s,e,i):
        if s == e:
            self.segtree[i] = [1,0] if self.nums[s] % 2 == 0 else [0,1]
            return self.segtree[i]

        m = int((s+e)/2)
        cal_lt = self.generate_seg_tree(s,m,i*2)
        cal_rt = self.generate_seg_tree(m+1,e,i*2+1)
        self.segtree[i] = [cal_lt[0]+cal_rt[0],cal_lt[1]+cal_rt[1]]
        return self.segtree[i]

    def get_oddeven_count(self,i,j,s,e,idx):
        if i==s and j==e:
            return self.segtree[idx]
        m = int((s+e)/2)
        if j <= m:
            return self.get_oddeven_count(i,j,s,m,2*idx)
        if i > m:
            return self.get_oddeven_count(i,j,m+1,e,2*idx + 1)
        cal_lt = self.get_oddeven_count(i,m,s,m,2*idx)
        cal_rt = self.get_oddeven_count(m+1,j,m+1,e,2*idx+1)

        return [cal_lt[0]+cal_rt[0],cal_lt[1]+cal_rt[1]]

    def upate_seg_tree(self,i,val,s,e,idx):

        if s==i and i == e:
            self.segtree[idx] = [1,0] if val % 2 == 0 else [0,1]
            return
        m = int((s+e)/2)
        if i > m:
            self.upate_seg_tree(i,val,m+1,e,2*idx+1)
        else:
            self.upate_seg_tree(i,val,s,m,2*idx)

        cal_lt = self.segtree[2*idx]
        cal_rt = self.segtree[2*idx + 1]

        self.segtree[idx] =  [cal_lt[0]+cal_rt[0],cal_lt[1]+cal_rt[1]]

        return




if __name__ == "__main__":

    n = int(input().strip())
    nums = list(map(int,input().strip().split(" ")))

    q = int(input())
    seg_tree = NumArray(nums)
    while q:
        t,i,j = map(int,input().strip().split(" "))
        if t in [1,2] :
            seg_tree.countRange(t,i-1,j-1)
        elif t==0:
            seg_tree.update(i,j)


        q=q-1





# 6
# 1 2 3 4 5 6
# 4
# 1 2 5
# 2 1 4
# 0 5 4
# 1 1 6













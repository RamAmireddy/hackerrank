class Heaps():

    def __init__(self, ls, op='min'):
        self.ls = [0] + ls
        try:
            self.op = op.lower()
        except:
            raise Exception("invalid operator \'" + self.op +"\'")
        self.n=len(self.ls)

        self.build_heapify()

    def comp(self, x, y):
        if self.op == 'min':
            return x < y
        elif self.op == 'max':
            return x > y
        else:
            raise Exception("invalid operator \'" + self.op +"\'")



    def heapify(self, i):
        if i > len(self.ls):
            return

        pos = i
        if 2 * i < self.n and self.comp(self.ls[2 * i], self.ls[pos]):
            pos = 2 * i
        if (2 * i + 1) < self.n and self.comp(self.ls[2 * i + 1],self.ls[pos]):
            pos = 2 * i + 1
        if pos != i:
            self.ls[pos],self.ls[i] = self.ls[i],self.ls[pos]
            self.heapify(pos)

    def build_heapify(self):

        for i in range(int(self.n / 2), 0, -1):
            self.heapify(i)

    def get_top(self): #max or min

        return self.ls[1] if self.n>1 else None





    def del_top(self):

        if self.n <=1:
            return None
        self.ls[1],self.ls[self.n-1] = self.ls[self.n-1],self.ls[1]
        x = self.ls[self.n-1]
        self.n -= 1
        self.ls = self.ls[:self.n]
        self.heapify(1)
        return x


    def del_i(self,i):
        if self.n <i:
            return None
        replace = (float('inf'),float('-inf'))[self.op == 'min']
        x = self.ls[i]
        self.ls[i] = replace
        self.ls[1],self.ls[i] = self.ls[i], self.ls[1]

        self.del_top()
        return x


    def __bottom_up(self,i):
        if i < 1:
            return
        pos = i
        if 2 * i < self.n and self.comp(self.ls[2 * i], self.ls[pos]):
            pos = 2 * i
        if (2 * i + 1) < self.n and self.comp(self.ls[2 * i + 1], self.ls[pos]):
            pos = 2 * i + 1
        self.ls[pos], self.ls[i] = self.ls[i], self.ls[pos]
        self.__bottom_up(int(i/2))



    def insert(self,x):
        self.ls.append(x)
        self.n += 1
        if self.n > 2:
            self.__bottom_up(int((self.n-1)/2))
    def sort(self):
        ans = []
        ls = self.ls.copy()
        x = self.del_top()
        while x:
            ans.append(x)
            x = self.del_top()

        self.ls = ls
        return ans






h = Heaps([49, 44, 46, 33, 35, 42, 27, 10, 26, 14, 31],op="min")

# print(h.ls,h.n)
print(h.sort())
   # 35

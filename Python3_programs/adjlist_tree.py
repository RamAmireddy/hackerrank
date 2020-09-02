# https://cses.fi/problemset/task/1131/
# https://cses.fi/problemset/task/1131
"""
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int findHt(vector < vector < int >> & alist, int & res, int root, int par){
    if (alist[root].size() == 1)
        return 0;
    vector < int > hts;
    for (int i=0;i < alist[root].size();i++){
        if (alist[root][i] != par){
            hts.push_back(findHt(alist, res, alist[root][i], root));
        }
    }
    sort(hts.begin(), hts.end());
    int len = hts.size();
    int dia = 1 + hts[len - 1];
    if (len > 1)
        dia += 1 + hts[len - 2];
    res = max(res, dia);
    return 1 + hts[len - 1];
    }
int main()
{
    int n, m,from, to;
    cin >> n;
    vector < vector < int >> alist(n + 1);
    alist[1].push_back(0);
    for (int i=0;i < n-1;i++){
        cin >>from >> to;
    alist[from].push_back(to);
    alist[to].push_back(from );
    }
    int res = 0;
    findHt(alist, res, 1, 0);
    cout << res << endl;
    return 0;
    }

"""


# class AdjListTree(object):
#
#     def __init__(self,n=0,adj_list=[[]]):
#         self.dia = 0
#
#         self.adj_list = adj_list
#
#     def get_height(self,root,par):
#
#         if len(self.adj_list[root]) == 1:
#             return 0
#
#         maxh = -1
#
#         for i in range(len(self.adj_list[root])):
#              if par != self.adj_list[root][i]:
#                 maxh = max(maxh,self.get_height(self.adj_list[root][i],root))
#
#         return maxh+1
dia = 0
adj_list = None
def get_dia(i, par):
    global dia
    global ls
    if len(adj_list[i]) == 1: return 0

    hts = []
    for j in range(len(adj_list[i])):
        if par != adj_list[i][j]:
            hts.append(get_dia(adj_list[i][j],i))

    hts.sort()
    x = 1+ hts[-1]
    if len(hts)>1:
        x += 1 + hts[-2]

    dia = max(dia,x)

    return 1+hts[-1]


"""
10
6 4
1 3
10 8
9 3
2 7
5 4
2 4
8 5
9 5
"""




n = int(input().strip())

ls = [[] for _ in range(n+1)]
p=0

ls[1].append(0)
for i in range(n-1):


    a,b = map(int,input().strip().split(" "))
    if i==0:
        p=a

    ls[a].append(b)
    ls[b].append(a)

adj_list = ls
get_dia(1,0)
print(dia)
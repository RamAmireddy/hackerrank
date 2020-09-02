# #include <iostream>
# #include <vector>
# #include <unordered_map>
#
# using namespace std;
# unordered_map<int,vector<int>> query;
#
# vector<int> dfs(vector<vector<int>> &alist,vector<int> &f,int root,int par){
# 	if(alist[root].size()==1){
# 		query[root][f[root]]++;
# 		return query[root];
# 	}
# 	vector<int> cur = query[root];
# 	cur[f[root]]++;
# 	for(int i=0;i<alist[root].size();i++){
# 		if(alist[root][i]!=par){
# 			vector<int> temp = dfs(alist,f,alist[root][i],root);
# 			for(int i=0;i<10;i++){
# 				cur[i]+=temp[i];
# 			}
# 		}
# 	}
# 	query[root] = cur;
# 	return cur;
# }
query = dict()
def dfs(alist,f,root,par):
    global query
    if len(alist[root]) == 1:
        query[root][f[root]]+=1
        return query[root]
    cur = query[root]
    cur[f[root]]+=1
    for i in range(len(alist[root])):
        if alist[root][i] != par:
            tmp = dfs(alist,f,alist[root][i],root)
            for j in range(10):
                cur[j] += tmp[j]
    query[root] = cur
    return cur



n = int(input().strip())
f = [0]+list(map(int,input().strip().split(" ")))
qf = [0 for i in range(10)]
alist = [[] for i in range(n+1)]
alist[1].append(0)
for i in range(n-1):
    frm,to = map(int,input().strip().split(" "))
    query[frm] = qf.copy()
    query[to] = qf.copy()
    alist[frm].append(to)
    alist[to].append(frm)
q = int(input().strip())
dfs(alist,f,1,0)
while q :
    q=q-1
    idx,val = map(int,input().strip().split())
    print(query[idx][val])

#
# int main()
# {
# 	ios_base::sync_with_stdio(false);
# 	cin.tie(NULL);
# 	int n,q,from,to,x,y,fn = 10;
# 	cin>>n;
# 	vector<int> f(n+1);
# 	vector<int> qf(fn,0);
# 	for(int i=1;i<=n;i++){
# 		cin>>f[i];
# 	}
# 	vector<vector<int>> alist(n+1);
# 	for(int i=1;i<n;i++){
# 		cin>>from>>to;
# 		query[from] = qf;
# 		query[to] = qf;
# 		alist[from].push_back(to);
# 		alist[to].push_back(from);
# 	}
# 	cin>>q;
# 	alist[1].push_back(0);
# 	dfs(alist,f,1,0);
# 	while(q--){
# 		cin>>x>>y;
# 		cout<<query[x][y]<<endl;
# 	}
# 	return 0;
# }
import os
import sys


#
# Complete the contacts function below.
#

class TNode:
    def __init__(self, cnt=0):
        self.cnt = cnt
        self.childs = [None for i in range(26)]


ans = 0


def add(root, st, i):
    if i == len(st):
        return

    if not root.childs[ord(st[i]) - ord('a')]:
        root.childs[ord(st[i]) - ord('a')] = TNode(1)
    else:
        root.childs[ord(st[i]) - ord('a')].cnt += 1
    add(root.childs[ord(st[i]) - ord('a')], st, i + 1)


def find(root, st, i):
    global ans
    if i == (len(st)):
        ans = root.cnt
        return
    elif not root.childs[ord(st[i]) - ord('a')]:
        ans = 0
        return
        # print(st[i],root.childs[ord(st[i])-ord('a')].cnt)
    find(root.childs[ord(st[i]) - ord('a')], st, i + 1)


def contacts(queries):
    global ans
    #
    # Write your code here.
    #
    root = TNode()
    ls = []
    for q in queries:
        ans = 0
        if q[0] == 'add':
            add(root, q[1], 0)
        elif q[0] == 'find':
            find(root, q[1], 0)
            ls.append(ans)

    return ls


if __name__ == '__main__':

    queries_rows = int(input())

    queries = []

    for _ in range(queries_rows):
        queries.append(input().rstrip().split())

    result = contacts(queries)

    print(result)

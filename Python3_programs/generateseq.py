ans = []


def swap(s, i, j):
    lst = list(s)
    lst[i], lst[j] = lst[j], lst[i]
    return ''.join(lst)


def gen(s, i, n):
    if i == n-1:
        ans.append(int(s))
    else:
        dupst=set()
        for j in range(i, n):
            if s[j] in dupst:
                continue
            dupst.add(s[j])
            st=swap(s, i, j)
            gen(st, i + 1, n)




def ceil(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    ceil = -1;
    while low <= high:
        mid = (low + high) // 2
        if (x < arr[mid]):
            ceil = arr[mid]
            high = mid - 1
        else:
            low = mid + 1
    return ceil


st = raw_input().strip()
for i in range(1, 5):
    num = "59" * i
    gen(num, 0, len(num));

ans.sort()

idx = ceil(ans, int(st));
print(idx)
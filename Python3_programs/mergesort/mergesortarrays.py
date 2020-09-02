def merge_arrays(ar1, ar2):
    ar = []
    k = 0
    l = 0
    while k < len(ar1) and l < len(ar2):
        if ar1[k] < ar2[l]:
            ar.append(ar1[k])
            k += 1
        else:
            ar.append(ar2[l])
            l += 1

    while k < len(ar1):
        ar.append(ar1[k])
        k += 1
    while l < len(ar2):
        ar.append(ar2[l])
        l += 1
    return ar


def mergesort(numbers, i, j):
    if i == j:
        return numbers[i]
    if i > j:
        return []
    mi = int((i + j) / 2)
    ar1 = mergesort(numbers, i, mi)
    ar2 = mergesort(numbers, mi + 1, j)
    mgarr = merge_arrays(ar1, ar2)
    return mgarr

import heapq
def merge(numbers):
    # code here
    # return merged list
    ans = []
    return mergesort(numbers,0,len(numbers)-1)



numbers = [[1, 2, 3],

             [4, 5, 6],

             [7, 8, 9]]
numbers = [[1, 2, 2, 2],

             [3, 3, 4, 4],

             [5, 5, 6, 6],

             [7, 8, 9, 9 ]]

print(merge(numbers))
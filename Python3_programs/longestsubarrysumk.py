t = int(raw_input().strip())
while t:
    n, k = map(int, raw_input().strip().split(" "))
    nums = list(map(int, raw_input().strip().split(" ")))

    mp = dict()
    mp[0] = -1
    l = 0
    for i in range(len(nums)):
        if i > 0:
            nums[i] += nums[i - 1]
        if nums[i] not in mp.keys():
            mp[nums[i]]=i
        if nums[i]-k in mp.keys():
            l = max(l, i - mp[nums[i] - k])

    print(l)

    t = t - 1
# code

t = int(input().strip())
while t:
    t = t - 1

    n = int(input().strip())
    st_times = list(map(int, input().strip().split(" ")))
    ed_times = list(map(int, input().strip().split(" ")))

    meet_timings = [[st_times[i], ed_times[i], i] for i in range(len(st_times))]
    del st_times, ed_times
    meet_timings.sort(key=lambda x: x[1])

    ans_ls = [[0,meet_timings[0][2] + 1]]

    for i in range(1, len(meet_timings)):
        if meet_timings[ans_ls[-1][0]][1] <= meet_timings[i][0]:
            ans_ls.append([i,meet_timings[i][2]+1])

    print(*ans_ls)




"""
1
6
1 3 0 5 8 5
2 4 6 7 9 9
"""
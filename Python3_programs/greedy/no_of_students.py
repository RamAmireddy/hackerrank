def run():
    s = int(input())
    times = []
    for i in range(s):
        s,e = map(int,input().strip().split(" "))
        times.append([s,e])
    # print(arivals,departures)
    if len(times) ==1:
        print(1)
    else:
        times.sort(key=lambda x: x[1])
        ans=2
        e1=times[0][1]
        e2 = times[1][1]

        for i in range(2, len(times)):
            x = min(e1,e2)
            if x<times[i][0]:
                ans+=1
                if x==e1:
                    e1=times[i][1]
                else:
                    e2=times[i][1]
        print(ans)
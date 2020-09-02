def get_maxval(val_wts,wt):
    price = 0
    i=0
    while wt:
        if wt >= val_wts[i][1]:
            wt = wt-val_wts[i][1]
            price = price + val_wts[i][0]

        else:
            f = wt/val_wts[i][1]
            price = price+f*val_wts[i][0]
            wt=0
        i=i+1
    return price

t = int(input().strip())

while t:
    t = t - 1
    n, wt = map(int, input().strip().split(" "))
    val_wt = list(map(int, input().strip().split(" ")))
    val_wts = []
    for i in range(0,len(val_wt), 2):
        val_wts.append([val_wt[i], val_wt[i + 1]])

    val_wts.sort(key=lambda x:x[0]/x[1], reverse=True)

    print(get_maxval(val_wts,wt))

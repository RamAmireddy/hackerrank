


arivals = list(map(int,"1 3 5".strip().split(" ")))
departures = list(map(int,"2 6 8".strip().split(" ")))
k = int(input())

arivals = [i + 1 for i in  arivals]
departures = [(-1*i) - 1 for i in  departures]
# print(arivals,departures)

meets = arivals + departures
print(meets)
meets.sort(key=lambda x:abs(x))
print(meets)
x = 0
ans = 0
for i in meets:
    if i>0:
        x = x + 1
        ans = max(x,ans)
    if i<0:
        x = x-1

print("No" if k<ans else "Yes")
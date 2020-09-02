# st=[]
# s=input().strip()
# for i in s:
#     if len(st) and st[-1]==i:
#         st.pop()
#     else:
#         st.append(i)
# if len(st):
#     print('NO')
# else:
#     print('YES')

def fractionToDecimal(numerator, denominator):
    """
    :type numerator: int
    :type denominator: int
    :rtype: str
    """
    isneg = True if (1.0 * numerator) / (1.0 * denominator)<0 else False

    if numerator < 0: numerator *= -1
    if denominator < 0: denominator *= -1

    integral = numerator / denominator
    rem = numerator % denominator
    ans = "-" if isneg else ""
    ans += str(integral)
    if rem:
        i = 0
        m = dict()
        tmp = ""
        while True:
            if rem < denominator:
                if tmp == '':
                    tmp = '.'
                else:
                    tmp += '0'
                i += 1
                m[rem] = i
                rem *= 10
            else:
                x = rem // denominator
                tmp += str(x)
                i += 1
                rem = rem % denominator
                if rem in m.keys():
                    break
                if rem == 0:
                    break
                else:
                    m[rem] = i
                    rem *= 10
        if rem != 0:
            y = m[rem]
            for j in range(i):
                if j == y:
                    ans += '('
                ans += tmp[j]
            ans += ')'
        else:
            ans += tmp;
    return ans

fractionToDecimal(22,7)
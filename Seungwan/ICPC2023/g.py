n, k = map(int, input().split())
frac_list = []

if k == 1:
    print(0, 1)
    exit()
if k == n:
    print(1, 1)
    exit()

for i in range(1, n+1):
    for j in range(i):
        if j == 0:
            continue
        gcd = 1
        for k in range(2, j+1):
            if j % k == 0 and i % k == 0:
                gcd = k
        frac_list.append([j//gcd, i//gcd])

frac_list = sorted(frac_list, key=lambda x: x[0]/x[1])
#중복 처리
frac_list = list(set(map(tuple, frac_list)))
print(frac_list[k-1][0], frac_list[k-1][1])
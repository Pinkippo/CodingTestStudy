n = int(input())

count = 0

for i in range(1, n+1):
    s = str(i)
    if s == s[::-1]:
        count += 1

print(count)

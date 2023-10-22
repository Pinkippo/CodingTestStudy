s = input()
sad_sum = 0
happy_sum = 0
result = 0
sad = ['S','A','D']
happy = ['H','A','P','Y'] 

for i in range(len(s)):
    if s[i] in sad:
        sad_sum += 1
    if s[i] in happy:
        happy_sum += 1

if(sad_sum - happy_sum == 0):
    result = 50.00
    #.00을 붙여주기 위해 round()함수 사용
    result = round(result, 2)
    result = format(result, ".2f")
else:
    result = happy_sum / (happy_sum + sad_sum) * 100
    result = round(result, 2)
    result = format(result, ".2f")

print(result)
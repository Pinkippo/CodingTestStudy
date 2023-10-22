'''

최소직사각형
https://school.programmers.co.kr/learn/courses/30/lessons/86491

'''

'''

1016 한승완 풀이
-> 각 명함의 배열을 돌면서 최대 가로, 세로 길이를 구한다.

'''

def solution(sizes):
    big = 0
    small = 0
    
    for i in sizes:
        if i[0] >= i[1]:
            if i[0] > big:
                big = i[0]
            if i[1] > small:
                small = i[1]
        else:
            if i[1] > big:
                big =i[1]
            if i[0] > small:
                small = i[0]
    answer = big * small
    return answer

'''

[실행 결과]
[[60, 50], [30, 70], [60, 30], [80, 40]]	4000

[시간복잡도]
= for문을 한 번 돌면서 최대 가로, 세로 길이를 구한다.
= O(n)

'''

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
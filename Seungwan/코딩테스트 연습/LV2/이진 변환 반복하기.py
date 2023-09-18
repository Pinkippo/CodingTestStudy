'''

이진 변환 반복하기
https://school.programmers.co.kr/learn/courses/30/lessons/70129

'''

'''

0918 한승완 풀이
- 문제에서 설명한 내용을 토대로 구현

'''
def solution(s):

    while_count = 0
    delete_zero = 0

    
    while(s != "1"):
        answer = ""
        while_count += 1

        x = ""
        for i in s:
            if(i == "1"):
                answer += "1"
            elif( i == "0"):
                delete_zero += 1
        s = format(len(answer), 'b')

    return [while_count, delete_zero]


print(solution("110100111"))
    
'''

모의고사
https://school.programmers.co.kr/learn/courses/30/lessons/42840

'''

'''

1016 한승완 풀이
-> 각 수포자의 찍는 패턴을 배열로 생성
-> 각 수포자의 정답 개수를 구한다.
-> 가장 많이 맞춘 사람을 구한다.

'''

def solution(answers):
    list1 = [1,2,3,4,5]
    list2 = [2,1,2,3,2,4,2,5]
    list3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0,0,0]
    answer = []
    
    for idx, x in enumerate(answers):
        if x == list1[idx%len(list1)]:
            score[0] += 1
        if x == list2[idx%len(list2)]:
            score[1] += 1
        if x == list3[idx%len(list3)]:
            score[2] += 1
            
    for idx, x in enumerate(score):
        if x == max(score):
            answer.append(idx+1)
    return answer

'''

[실행 결과]
[1, 2, 3, 4, 5]	[1]
[1, 3, 2, 4, 2]	[1,2,3]

[시간복잡도]
= for문을 한 번 돌면서 각 수포자의 정답 개수를 구한다.
= O(n)

'''

print(solution([1,2,3,4,5]))
'''

조이스틱
https://school.programmers.co.kr/learn/courses/30/lessons/42860?language=python3

'''

'''

0924 ~ 0925 한승완 풀이

- 조이스틱을 위 아래로 움직이는 것은 알파벳을 바꾸는 것이므로 알파벳을 바꾸는데 드는 최소 횟수를 구하면 됨 -> easy
- 조이스틱을 좌우로 움직이는 것은 A를 건너 뛸 수 있으므로 A가 아닌 문자가 연속으로 나오는 구간을 찾아서 최소 횟수를 구하면 됨 -> hard

'''

def solution(name):
    answer = 0 # 알파벳을 바꾸는데 드는 최소 횟수
    min_move  = len(name) - 1 # 최소 좌우 이동 횟수 -> 기본 설정 
    
    '''
    알파벳 배열 -> 다른 방식으로 구현 가능하지만 실력 부족으로 이렇게 구현함
    '''
    dicktionory = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I','J', 'K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    '''
    알파벳 이동 조이스틱 이동 횟수 계산
    '''
    for i in range(len(name)):
        if name[i] == 'A':
            continue
        else:
            answer += min(dicktionory.index(name[i]), 26 - dicktionory.index(name[i])) # 위 아래 최소 이동 횟수 계산

    '''

    https://velog.io/@jqdjhy/프로그래머스-파이썬-조이스틱-Greedy

    커서 부분 보고 해결한 부분 -> 솔직히 이해는 되는데 100% 이해는 안됨
    
    다른 방법 -> DFS로 풀 수 있음 

    '''
    for i in range(len(name)):
        next = i + 1
        while next < len(name) and name[next] == 'A': # A가 나오면 다음으로 넘어감
            next += 1
        min_move = min([min_move, 2 * i + len(name) - next, i + 2 * (len(name) -next)]) 

    answer += min_move
    return answer


print(solution("JEROEN"))
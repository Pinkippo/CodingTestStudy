'''

큰 수 만들기
https://school.programmers.co.kr/learn/courses/30/lessons/42883?language=python3

'''

'''

0925 한승완 풀이 [1]
-> k번동안 왼쪽에서 오른쪽으로 커서를 이동하면서 최대값을 찾는다.

[ 시간 초과 ]
-> 8번 10번 테스트 케이스에서 시간 초과 발생
-> 솔직히 개 억지인거 같음

'''
def solution2(number, k):
    answer = []
    number_len = len(number)
    number = list(number)  # 문자열을 리스트로 변환

    for i in range(number_len - k):
        max_num = 0
        max_idx = 0
        for j in range(i, i + k + 1):
            value = int(number[j])
            if value > max_num:
                max_num = value
                max_idx = j
        
        k -= max_idx - i  # 선택한 숫자를 제외한 숫자 개수 업데이트
        answer.append(str(max_num))

    return ''.join(answer)


'''

0925 한승완 풀이 [2]
-> k번동안 왼쪽에서 오른쪽으로 커서를 이동하면서 최대값을 찾는다.
-> + 최대값을 찾을 때, 9가 나오면 바로 종료한다.

[ 성공 ]

'''

def solution(number, k):
    answer = []
    number_len = len(number)
    to_remove = number_len - k  

    '''
    to_remove: 제거할 숫자 개수 / start: 최대값을 찾을 때, 시작할 인덱스
    '''
    start = 0
    for i in range(to_remove):
        max_num = -1
        end = number_len - to_remove + i + 1
        for j in range(start, end): # start ~ end-1 까지
            value = int(number[j])
            if(value == 9): # 최대값이 9이면 바로 종료
                max_num = value
                start = j + 1
                break
            elif value > max_num: # 최대값이 9가 아니면 최대값 업데이트
                max_num = value
                start = j + 1  # 다음 숫자는 현재 찾은 최대 숫자 이후부터 시작

        answer.append(str(max_num))

    return ''.join(answer)


print(solution("1231234", 3))

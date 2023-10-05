'''

의상
https://school.programmers.co.kr/learn/courses/30/lessons/42578

'''

'''

1005 한승완 풀이

- 파이썬의 딕셔너리를 이용해서 키 밸류를 통해 의상별 개수를 확인
- 경우의 수를 계산

'''
def solution(clothes):
    ans = 1
    clothes_dict = {}

    '''
    옷의 종류별 딕셔너리 생성
    ex. {'headgear': 2, 'eyewear': 1}
    '''
    for cloth in clothes:
        clothes_dict[cloth[-1]] = 0

    '''
    clothes를 탐색하며 옷의 개수만큼 추가
    '''
    for cloth in clothes:
        clothes_dict[cloth[-1]] += 1
        
    '''
    딕셔너리의 values를 탐색하면서 정답 도출
    '''
    for value in clothes_dict.values():
        ans += value * ans

    '''
    아무것도 입지 않는 것은 존재하지 않으므로 (-1) 수행
    '''
    return ans -1 


'''

- [ 시간복잡도 ]
- O(N)

'''

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
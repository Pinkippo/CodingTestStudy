'''

여행경로
https://school.programmers.co.kr/learn/courses/30/lessons/43164

'''

'''

0922 한승완 풀이

- BFS로 탐색하여 경로 찾고 배열에 추가

- 방문 여부는 항공편 자체를 이용
- BFS 탐색을 할때 항공편의 도착지가 다른 항공편의 출발지와 일치할떄 추가
    - BUT 알파벳 순으로 해야한다가 조금 걸리긴함

- [ 시간 초과 ] -> 아무래도 다른 방식이 있는듯 함 + 알파벳 순 정렬도 못했음

'''

from collections import deque

def solution2(tickets):
    answer = ["ICN"]

    bool_ticket = [0] * len(tickets)

    queue = deque()
    queue.append(tickets[0])
    bool_ticket[0] = 1

    while queue:
        now_ticket = queue.popleft()
        answer.append(now_ticket[1])

        for index, future_ticket in enumerate(tickets):
            if(now_ticket[1] == future_ticket[0] and bool_ticket[index] == 0):
                queue.append(future_ticket)

    return answer


'''

0922 한승완 풀이
- 질문을 보다가 딕셔너리로 풀어보라는 얘기를 확인
    -> 출발 : [도착, 도착, 도착] 형태의 딕셔너리로 중복을 처리할 수 있겠다 판단

'''

def solution(tickets):

    '''
    딕셔너리 생성
    '''
    route = {} 

    '''
    딕셔너리에 티켓 정보를 -> "출발" : ["도착", "도착" ... ] 형태 저장
    '''
    for ticket in tickets:
        route[ticket[0]] = route.get(ticket[0], []) + [ticket[1]]
    
    '''
    value 값들을 알파벳 역순으로 정렬
    '''
    for r in route:
        route[r].sort(reverse=True)
    
    route_stack = ['ICN']
    answer = []

    '''
    스택을 이용한 DFS
    '''
    while route_stack:
        if route_stack[-1] in route and route[route_stack[-1]]: # 딕셔너리에 키가 있고, 그 키의 value가 존재할때
            route_stack.append(route[route_stack[-1]].pop()) # value의 마지막 값을 스택에 추가
        else:
            answer.append(route_stack.pop())

    return answer[::-1] # 역순으로 저장되어 있으므로 반대로 출력



'''

테스트

'''
# 예상 결과 - ["ICN", "JFK", "HND", "IAD"]
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])) 
'''

네트워크
https://school.programmers.co.kr/learn/courses/30/lessons/43162

'''

'''

0919 한승완 풀이 
- DFS/ BFS 던 컴퓨터들을 탐색하면서 끊기면 1 추가

- 11/13 테스트케이스 성공
- 2/13 테스트케이스 실패

-> 오류 원인 : 큐 내부를 탐색할 때 while을 사용하지 않고 직접 for문을 돌려서 큐 내부를 탐색하지 못함
-> 해결 방법 : 큐 내부를 탐색할 때 while을 사용하여 큐 내부를 탐색하고 상위에서 for문을 돌려사용

'''

from collections import deque

def solution2(n, computers):

    if(n == 1):
        return 1

    bool_computers = [0] * n

    def bfs():
        answer = 0
        queue = deque()

        queue.append([ 0 , computers[0]])
        bool_computers[0] = 1

        for k in range(n+1):

            if(len(queue) == 0):
                answer += 1
                for index , computer in enumerate(computers):
                    if(bool_computers[index] == 0):
                        queue.append([index, computer])
                        bool_computers[index] = 1
                        break
            else:
                networks = queue.popleft()
            
                for index , computer in enumerate(networks[1]):
                    if(index == networks[0] and sum(networks[1]) == 1):
                        answer += 1
                        continue
                    elif(computer == 1 and bool_computers[index] == 0 and index != networks[0]):
                        queue.append([index, computers[index]])
                        bool_computers[index] = 1

                if(k == n - 1 and len(queue) == 0 and sum(networks[1]) != 1):
                    answer += 1
                    break
        
        return answer
    
    return bfs()
'''

0919 한승완 풀이

- BFS 이용

- 성공

'''

def solution(n, computers):

    '''
    컴퓨터가 1개일 때 1 리턴
    '''
    if n == 1:
        return 1

    '''
    방문한 컴퓨터를 체크할 배열
    '''
    bool_computers = [0] * n

    '''
    BFS 탐색
    '''
    def bfs(computer):
        queue = deque() # 큐 생성
        queue.append(computer) # 시작 컴퓨터를 큐에 삽입
        bool_computers[computer] = 1 # 시작 컴퓨터를 방문했다고 체크

        while queue: # 큐가 빌 때까지 반복
            current = queue.popleft() # 큐에서 하나를 꺼냄
            
            for index, value in enumerate(computers[current]): # 꺼낸 컴퓨터와 연결된 컴퓨터를 탐색
                if value == 1 and bool_computers[index] == 0: # 연결된 컴퓨터가 방문하지 않은 컴퓨터일 때
                    queue.append(index) # 큐에 삽입
                    bool_computers[index] = 1 # 방문 체크

    '''
    탐색 시작
    '''
    answer = 0
    for i in range(n): # 모든 컴퓨터를 탐색
        if bool_computers[i] == 0:
            '''
            방문하지 않은 컴퓨터일 때 BFS 탐색으로 네트워크를 돌며 방문 체크 후 answer += 1
            '''
            bfs(i)
            answer += 1
    return answer


#print(solution(4, [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]))
print(solution2(	3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
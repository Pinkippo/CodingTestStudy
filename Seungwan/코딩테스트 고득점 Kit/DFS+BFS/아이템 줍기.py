'''

아이템 줍기
https://school.programmers.co.kr/learn/courses/30/lessons/87694

'''

'''

0921 한승완 풀이
- BFS로 탐색하면서 아이템 위치를 탐색하고, 아이템 위치를 찾으면 정답을 반환

- [ 성공 ]

'''

from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):


    answer = 0

    dx = [0, 1, 0, -1] # x 이동
    dy = [1, 0, -1, 0] # y 이동

    '''
    테두리를 처리하기 위해 2차원 배열을 102 * 102로 만듬 -> 최단거리 상에서 테두리를 처리할 수 있게 됨
    bool_map은 방문 여부를 체크
    '''
    line_map = [[-1] * 102 for i in range(102)]
    bool_map = [[1] * 102 for _ in range(102)]
    bool_map[characterY][characterX] = 1
    
    '''
    직사각형 그리기
    '''
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: x*2, r)
        '''
        직사각형의 테두리를 1로 채우고 내부를 0으로 채움
        '''
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
            	# x1, x2, y1, y2는 테두리이므로 제외하고 내부만 0으로 채움
                if x1 < i < x2 and y1 < j < y2:
                    line_map[i][j] = 0
                # 다른 직사각형의 내부가 아니면서 테두리일 때 1로 채움
                elif line_map[i][j] != 0:
                    line_map[i][j] = 1

    queue = deque()
    '''
    시작점을 2배하여 큐에 추가
    '''
    queue.append([characterX * 2, characterY * 2])

    while queue:
        x, y = queue.popleft()
        
        '''
        만약 현재 좌표가 아이템의 위치라면 해당 방문 좌표의 지점의 값을 2로 나눈 몫을 반환
        '''
        if x == itemX * 2 and y == itemY * 2:
            answer = bool_map[x][y] // 2
            break
        
        '''
        상하좌우 탐색
        '''
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            '''
            만약 새로운 위치가 테두리이고 방문하지 않았다면 큐에 추가하고 방문처리
            '''
            if line_map[nx][ny] == 1 and bool_map[nx][ny] == 1:
                queue.append([nx, ny])
                '''
                현재 위치의 방문 여부를 이전 위치의 방문 여부 + 1로 처리하여 이동 거리를 계산
                '''
                bool_map[nx][ny] = bool_map[x][y] + 1
 
    return answer

'''

솔직히 3레벨 많이 어려운거같음

-> 테두리를 처리한다는 아이디어가 없었다면 풀지 못했을 것 같음
-> 아이디어적으로 더 생각하고 풀이할 것

'''

print(solution([[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]],9,7,6,1))
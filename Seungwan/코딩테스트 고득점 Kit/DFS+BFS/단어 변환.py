'''

단어 변환
https://school.programmers.co.kr/learn/courses/30/lessons/43163

'''

'''

0920 한승완 풀이
- BFS로 탐색하면서 words 내부에 있는 단어들을 탐색하고 target과 같으면 answer에 저장

- [ 실패 ]

'''

from collections import deque

def solution2(begin, target, words):
    
    bool_words = [0] * len(words)

    def bfs(start, target):

        queue = deque()
        queue.append(start)

        while queue:
            print("while")
            before_word = queue.popleft()
            
            for_test_num = 0

            for index, after_word in enumerate(words):
                print("for")
                begin_word_num = len(start)
                test_num = 0

                for before_char , after_char in zip(before_word, after_word):
                    if(before_char != after_char):
                        print("not match")
                        test_num += 1
                
                if(test_num == 1 and bool_words[index] == 0 ):
                    print("change")
                    bool_words[index] = 1
                    for_test_num += 1
                    queue.append(words[index])
                    if(words[index] == target):
                        print("동일")
                        return len(bool_words)
                    break
                    
    
            if(for_test_num == 0 and len(queue) == 0):
                print("반환")
                return 0
    
    return bfs(begin, target)

'''

0920 한승완 풀이 - [2]
- BFS로 탐색하면서 words 내부에 있는 단어들을 탐색하고 target과 같으면 answer에 저장
- [ 성공 ]

'''

def solution(begin, target, words):


    '''
    단어 목록에 target이 없으면 0 반환
    '''
    if target not in words:
        return 0

    answer = 0
    queue = deque()
    queue.append([begin,0])
    bool_words = [0] * len(words)
    
    while queue:
        word, cnt = queue.popleft()
        if word == target: # target과 같으면 answer에 저장하고 break
            answer = cnt # answer에 저장
            break        
        for i in range(len(words)): # words 내부에 있는 단어들을 탐색
            temp_cnt = 0
            if not bool_words[i]: # 방문하지 않은 단어일 때
                for j in range(len(word)): # 단어의 길이만큼 반복하면서 다른 문자가 1개인지 확인
                    if word[j] != words[i][j]:
                        temp_cnt += 1
                if temp_cnt == 1: # 다른 문자가 1개일 때
                    queue.append([words[i], cnt+1]) # 큐에 삽입
                    bool_words[i] = 1 # 방문 체크
                    
    return answer

'''

[테스트]

'''

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
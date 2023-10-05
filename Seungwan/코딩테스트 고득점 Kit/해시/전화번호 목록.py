'''

전화번호 목록
https://school.programmers.co.kr/learn/courses/30/lessons/42577

'''

'''

1005 한승완 풀이 - [1]
- 짧은 내용부터 정렬
- 정렬된 배열을 탐색하며 같은 접두어인지 확인
- 같은 접두어가 존재하면 False 반환


- [ 시간 초과 ]

'''
def solution2(phone_book):
    phone_book.sort()

    for i in range(len(phone_book)):
        for j in range(i+1, len(phone_book)):
            if phone_book[i] == phone_book[j][:len(phone_book[i])]:
                return False

    return True

'''

1005 한승완 풀이 - [2]
- 딕셔너리를 이용해서 키 밸류를 통해 접두어인지 확인
- 접두어가 존재하면 False 반환

'''
def solution(phone_book):
       
    '''
    딕셔너리 생성
    '''
    phone_book_dict = {}

    '''
    딕셔너리에 전화번호를 키로 추가
    '''
    for phone in phone_book:
        phone_book_dict[phone] = 0

    '''
    딕셔너리의 키를 탐색하면서 접두어가 존재하는지 확인
    '''
    for phone in phone_book:
        for i in range(1, len(phone)):
            if phone[:i] in phone_book_dict:
                return False

    return True


'''

- [ 시간복잡도 ]

- solution2 : O(N^2) 
- solution : O(N^2)

- 왜 시간초과가 안나는지 모르겠음 


'''

'''

3. 다른 사람의 풀이

'''
def solution3(phone_book):
    
    '''
    파이썬의 문자열 정렬은 사전순으로 정렬되므로 접두어가 존재하면 바로 다음 전화번호와 비교하면 됨!
    '''
    phone_book.sort()

    '''
    현재 전화번호와 다음 전화번호를 비교하여 접두어인지 확인
    '''
    for i in range(len(phone_book) - 1):
        if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
            return False

    return True





print(solution(["119", "97674223", "1195524421"]))
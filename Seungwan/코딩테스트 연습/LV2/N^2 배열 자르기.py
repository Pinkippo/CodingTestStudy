'''

N^2 배열 자르기
https://school.programmers.co.kr/learn/courses/30/lessons/87390

'''

'''

0918 한승완 풀이 [1]
- 문제에서 설명한 내용을 토대 -> 재귀 구현

- [ 시간초과 ]

'''

def solution2(n, left, right):

    x = []

    def makeList(index):
        for i in range(index, n+1):
            if(i == index):
                x.extend([i] * index)
            else:
                x.extend([i])
        
        if(index < n):
            makeList( index +1)
        else:
            return
        
    makeList(1)

    return  x[left:right+ 1]


'''

0918 한승완 풀이 [2]
- 문제에서 설명한 내용을 토대 -> 일반적으로 수열을 만들어서 풀기

- [ 시간초과 ] -> 35.0

- 이중 포문을 이용하여 슬라이싱했음

'''

def solution3(n, left, right):

    x = []

    for i in range(1, n+1):
        x.extend([i] * i)
        for j in range(i+1,n+1):
            x.extend([j])

    return  x[left:right+ 1]

'''

0918 한승완 풀이 [3]

- 문제에서 설명한 내용을 토대 -> 일반적으로 수열을 만들어서 풀기

- left / rigth 조건이 되게 꺼림직 함을 느낌

- 2시간 생각해보니 수학적으로 가능할거 같음
- 근데 어떻게 만들지는 모르겠음 -> 조금 찾아봤음
- max(left // n, left % n )+1 ~ max(right // n, right % n )+1 까지의 수열 이용

'''

def solution(n, left, right):

    x = []

    for i in range(left, right+1):
        x.append(max(i // n, i % n )+1)

    return  x


print(solution(4,7,14))

'''

솔직히 3레벨 급이라고 생각함

'''




'''

체육복
https://school.programmers.co.kr/learn/courses/30/lessons/42862

'''

'''

0923 한승완 풀이

- 학생 수 만큼 1을 가진 배열 생성
- lost에 해당하는 학생 = -1, reserve에 해당하는 학생 = +1

-> 학생 수 만큼 배열을 탐색, 0인 학생을 찾아 앞 뒤 학생이 여벌의 체육복을 가지고 있는지 확인 후 적용

'''

def solution(n, lost, reserve):

    bool_student = [1] * n  # 학생 수 만큼 1을 가진 배열 생성

    for i in lost:
        bool_student[i-1] -= 1 # lost에 해당하는 학생 = -1
    
    for i in reserve:
        bool_student[i-1] += 1 # reserve에 해당하는 학생 = +1

    '''
    학생 수 만큼 배열을 탐색 -> 0인 학생을 찾아 앞 뒤 학생이 여벌의 체육복을 가지고 있는지 확인 후 적용
    '''
    for i in range(n):
        if bool_student[i] == 0:
            if i != 0 and bool_student[i-1] == 2:
                bool_student[i] += 1
                bool_student[i-1] -= 1
            elif i != n-1 and bool_student[i+1] == 2:
                bool_student[i] += 1
                bool_student[i+1] -= 1
    
    return n - bool_student.count(0) # 체육복이 없는 학생 수를 제외한 학생 수 반환

'''

[테스트]
n = 5
lost = [2, 4]
reserve = [1, 3, 5]

[시간 복잡도]
O(n) -> 학생 수 만큼 배열을 탐색

'''

print(solution(5,[2, 4],[1, 3, 5]))
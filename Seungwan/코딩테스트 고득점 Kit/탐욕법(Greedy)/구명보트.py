'''

구명보트
https://school.programmers.co.kr/learn/courses/30/lessons/42885

'''

'''

0926 한승완 풀이
- 정렬 후 왼쪽과 오른쪽을 비교해서 더한 값이 limit보다 작으면 둘 다 태움 -> 전체 인원에서 2명씩 탄 사람의 수를 뺀 값이 구명보트의 개수
- 더한 값이 limit보다 크면 왼쪽만 태움

- [ 성공 ]

- 정렬 + 투 포인터 문제 -> 정렬을 하면 투 포인터를 사용할 수 있는 문제가 많음

'''

def solution(people, limit) :
    
    many_people_in = 0
    people.sort() #정렬 

    left = 0 #무게 적은쪽 커서
    right = len(people) - 1 #무게 많은쪽 커서

    while left < right : # 무게 적은쪽 커서가 무게 많은쪽 커서보다 작을 때까지 반복

        if people[right] + people[left] <= limit : # 두 사람의 무게 합이 limit보다 작으면 왼쪽 오른쪽 모두 탑승
            left += 1
            many_people_in += 1

        right -= 1 # 아닐 경우 오른쪽만 탑승

    return len(people) - many_people_in # 구명보트의 개수는 전체 사람의 수에 여러명이 함께 탄 사람의 수를 뺀 값


'''

- [ 시간복잡도 ]
- O(NlogN) => 정렬(NlogN) + while(N)

'''

print(solution([70, 50, 80, 50], 100)) 

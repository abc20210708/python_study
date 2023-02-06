# 국영수 

n = int(input())
students = [] # 학생 정보를 담을 리스트

# 모든 학생의 정보를 입력 받기
for _ in range(n):
    students.append(input().split())
    
students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

# 정렬된 학생 정보에서 이름만 출력
for i in students:
    print(i[0])
    
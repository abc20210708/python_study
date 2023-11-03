## 한 줄로 서기 (실버 2)
import sys
input = sys.stdin.readline
## 다른 풀이 
#  참고 블로그 https://ryu-e.tistory.com/26

n = int(input())
arr = list(map(int, input().split()))
result = [0] * n

# 1. 키 작은 사람부터 결과 넣기
for i, a in enumerate(arr):
    cnt = 0  # 앞에 키큰 사람 넣은 횟수
    print(f"i : {i}")
    print(f"a : {a}")
    for j, res in enumerate(result):
        print(f"j : {j}")
        print(f"res : {res}")
        # 2. 아직 아무도 안 채워지고, 
        # 앞에 키 큰 사람으로 더 채워야하는 경우: cnt 늘리기
        if res == 0 and cnt < a:
            cnt += 1
         # 3. 아직 아무도 안 채워지고, 
         # cnt 와 a가 동일한 경우: 현재 학생 넣기
        elif res == 0 and cnt == a:
            result[j] = i + 1
            break
print(*result)


#  참고 블로그 https://fre2-dom.tistory.com/400

n = int(input())
lst = list(map(int, input().split()))
res = [0] * n

# 반복문을 통해 각 자리에 들어갈 사람을 확인
for i in range(n):
    cnt = 0 # 자신의 왼쪽의 키 큰 사람 수
    # 반복문을 통해 모든 사람을 확인
    for j in range(n):
        # 자신의 왼쪽 키 큰 살마의 수가 맞고 그 자리에 아무도 없다면
        if cnt == lst[i] and res[j] == 0:
            res[j] = i + 1
            break
        # 자리에 아무도 없다면 자신의 왼쪽 키 큰 사람 수 카운트
        elif res[j] == 0:
            cnt += 1
            
print(*res)
# print(' '.join(map(str, res)))
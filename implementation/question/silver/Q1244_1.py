# 스위치 켜고 끄기 (실버 4) 다른 풀이

# 참고 블로그
# https://dogsavestheworld.tistory.com/entry/python-%EB%B0%B1%EC%A4%80-1244%EB%B2%88-%EC%8A%A4%EC%9C%84%EC%B9%98-%EC%BC%9C%EA%B3%A0-%EB%81%84%EA%B8%B0

n = int(input())
# idx 값 맞추기 위해 0번에 미지값 추가
s = [-1] + list(map(int, input().split()))
k = int(input())
students = [tuple(map(int, input().split())) for _ in range(k)]

for g, num in students:
    # 성별이 남자일때
    if g == 1:
        for i in range(num, n+1, num):
            s[i] = 1 - s[i]
    # 성별이 여자일때
    else:
        s[num] = 1 - s[num]
        for k in range(n//2):
            if num + k > n or num - k < 1: break
            if s[num+k] == s[num-k]:
                s[num+k] = 1 - s[num+k]
                s[num-k] = 1 - s[num-k]
            else:
                break  

for i in range(1, n+1):
    print(s[i], end=' ')
    if i % 20 == 0:
        print()
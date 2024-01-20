## K-세준수 (실버 5)
#  참고 블로그 https://velog.io/@bonglet/%EB%B0%B1%EC%A4%80-1418-K-%EC%84%B8%EC%A4%80%EC%88%98
#  https://maeseok.tistory.com/305
import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
#  #01 : 2부터 n까지 리스트 s에 소인수분해한 값 중 가장 큰 값을 저장
s = [0 for i in range(n+1)]
for i in range(2, n+1):
    if s[i] == 0:
        for t in range(i, n+1, i):
            if t % i == 0:
                s[t] = max(s[t], i)
# 02 : 만약 i가 k보다 작은 값이라면 ans에 1을 더한다.
# s는 처음 시작값이 0이기에 출력할 때 1을 빼고 ans를 출력

ans = 0
for i in s:
    if i <= m:
        ans += 1
print(ans-1)
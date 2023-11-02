## 수들의 합 (실버 4)
#  참고 블로그 https://my-coding-notes.tistory.com/225

n, m = map(int, input().split())
a = list(map(int, input().split()))

i, j, cnt, total = 0, 0, 0, 0

while 1:
    if total >= m:
        total -= a[i]
        i += 1
    elif j == n:
        break
    else:
        total += a[j]
        j += 1

    if total == m:
        cnt += 1

print(cnt)


'''
if j == n:로 바꾼다면,
if j == n: 부분이 항상 참(True)이 됩니다. 
그 결과로 while 루프가 j가 n에 도달하더라도 
바로 종료되어버리게 됩니다. 

이렇게 되면 모든 부분 리스트를 검사하기 전에 루프가 끝나버립니다.

따라서 elif j == n:를 유지하는 것이 중요하며, 
elif는 이전 조건에 만족하지 않을 때만 실행되도록 하는데 도움을 줍니다.
'''
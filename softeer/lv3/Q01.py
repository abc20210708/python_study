## 성적 평균 *

#  다른 풀이
#  참고 블로그 https://jie0025.tistory.com/436
import sys
input = sys.stdin.readline

n, k = map(int,input().split())
scores = [0] + list(map(int,input().split()))

for i in range(1, n+1): #누적합 만들기
    scores[i] += scores[i-1]

for i in range(k):
    start, end = map(int,input().split())
    num = end - start +1
    if (start == 1): 
        result = scores[end] / num
    else: 
        result = (scores[end] - scores[start-1]) / num

    #print(round(result, 2))  # 반올림하는 함수라서 값이 없을 수도 있음 -> 45.0
    print(f'{result:.2f}') #값이 없으면 0으로 채워주는 친구 -> 45.00




n, k = map(int, input().split())
s = [0] + list(map(int, input().split()))
result = []

for i in range(k):
    sum = 0
    a, b = map(int, input().split())
    x = s[a:b+1]

    for j in x:
        sum += j
    result.append(round(sum/len(x), 2))

for i in result:
    print(format(i, ".2f")) # 참고 블로그 https://blockdmask.tistory.com/534
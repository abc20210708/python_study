## 연속 부분 최대곱 (실버 4)
#  참고 블로그 https://velog.io/@deannn/BOJ-%EB%B0%B1%EC%A4%80-2670%EB%B2%88-%EC%97%B0%EC%86%8D%EB%B6%80%EB%B6%84%EC%B5%9C%EB%8C%80%EA%B3%B1-Python

N = int(input())
arr = list(float(input()) for _ in range(N))
for i in range(1, N):
    arr[i] = max(arr[i], arr[i] * arr[i - 1])
print('%0.3f' % max(arr))

## 실수형 출력
#  참고 블로그 https://sylagape1231.tistory.com/42

'''
실수형 변수를 소수점 맞춰 출력하기

.4f == 소수 4째 자리까지 반올림 출력
  변수 포멧 (%d, %s, ...) 이용
   -%를 이용한다.

x = 3.141592653
print("%.4f" % x)
▼ 출력 결과
3.1416
'''
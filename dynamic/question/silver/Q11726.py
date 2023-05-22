## 2xn 타일링 (실버 3) *
# 참고 블로그 https://velog.io/@tkdduf727/%EB%B0%B1%EC%A4%80-2n-%ED%83%80%EC%9D%BC%EB%A7%81-11726%EB%B2%88-%ED%8C%8C%EC%9D%B4%EC%8D%AC-Python-%EB%8B%A4%EC%9D%B4%EB%82%98%EB%AF%B9-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D
# https://datazzang.tistory.com/19

n = int(input())
res = [i + 1 for i in range(n)]

# 2이하는 숫자를 그대로 출력
if n <= 2:
    print(n)
else:
    for i in range(3, n):
        res[i] = res[i-1] + res[i-2]
    print(res[n-1] % 10007)
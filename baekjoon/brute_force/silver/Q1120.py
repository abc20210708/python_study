## 문자열 (실버 4)
#  참고 블로그 https://velog.io/@yj_lee/%EB%B0%B1%EC%A4%80-1120%EB%B2%88-%EB%AC%B8%EC%9E%90%EC%97%B4-%ED%8C%8C%EC%9D%B4%EC%8D%AC
a, b = map(str, input().split())

res = []
for i in range(len(b)-len(a)+1):
    cnt = 0
    for j in range(len(a)):
        if a[j] != b[j+i]:
            cnt += 1
    res.append(cnt)
print(min(res))
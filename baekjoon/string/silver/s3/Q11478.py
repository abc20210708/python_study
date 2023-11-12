## 서로 다른 부분 문자열의 개수 (실버 3)
#  참고 블로그 https://velog.io/@yj_lee/%EB%B0%B1%EC%A4%80-11478%EB%B2%88-%EC%84%9C%EB%A1%9C-%EB%8B%A4%EB%A5%B8-%EB%B6%80%EB%B6%84-%EB%AC%B8%EC%9E%90%EC%97%B4%EC%9D%98-%EA%B0%9C%EC%88%98-%ED%8C%8C%EC%9D%B4%EC%8D%AC
import sys


res = set()
str = input().rstrip()

for i in range(len(str)):
    for j in range(i, len(str)):
        res.add(str[i:j+1]) # i번째 문자부터 부분 문자열 구하기
        
print(len(res))

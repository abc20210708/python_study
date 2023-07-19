## 포도주 시식

# 참고 블로그 https://myjamong.tistory.com/313
#            https://velog.io/@bye9/%EB%B0%B1%EC%A4%80%ED%8C%8C%EC%9D%B4%EC%8D%AC-2156-%ED%8F%AC%EB%8F%84%EC%A3%BC-%EC%8B%9C%EC%8B%9D


n = int(input())
arr = [0] * 10000
for i in range(n):
    arr[i] = int(input())
    
d = [0] * 10000
d[0] = arr[0]
d[1] = arr[0] + arr[1]
d[2] = max(arr[2] + arr[0], arr[2]+arr[1], d[1])

for i in range(3, n):
    d[i] = max(arr[i] + d[i-2], arr[i]+arr[i-1]+d[i-3], d[i-1])
    
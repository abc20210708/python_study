## 오셀로 재배치 (실버 4)
#  참고 블로그 https://jobdong7757.tistory.com/145
t = int(input())
arr, res = [], []
cnt = 0

for i in range(t):
    n = int(input())
    first = input()
    second = input()
    
    for i in range(n):
        if first[i] != second[i]:
            arr.append(first[i])
    if arr.count('B') >= arr.count("W"):
        cnt = arr.count("B")
    else:
        cnt = arr.count("W")
    res.append(cnt)
    arr = []
    
for a in res:
    print(a)
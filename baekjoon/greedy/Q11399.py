# ATM
## 참고 블로그 https://puleugo.tistory.com/24

n = 5
arr = [3, 1, 4, 3, 2]

arr.sort()

s = 0

for i in range(1, n+1):
    s += sum(arr[0:i])
    
print(s)

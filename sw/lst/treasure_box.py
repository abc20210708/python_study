## 보물 상자
#  참고 블로그 https://stopthebackspace.tistory.com/23

t = int(input())

for tc in range(t):
    n, k = map(int, input().split())
    length = n // 4
    target = input().rstrip()
    target += target
    
    nums = set()
    
    for i in range(n):
        tmp = target[i:i+length]
        nums.add(int(tmp, 16))
        
    nums = sorted(list(nums), reverse=True)[k-1]
    print(f"#{tc+1} {nums}")
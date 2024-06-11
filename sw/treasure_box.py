## 보물 상자
#  참고 블로그 https://stopthebackspace.tistory.com/23

t = int(input())

for case in range(1, t+1):
    n, k = map(int, input().split())
    hexa_str = input()
    hexa_str += hexa_str
    
    nums = set()
    num_len = n // 4 
    
    for i in range(0, n):
        hexa_num = hexa_str[i:i+num_len]
        tmp = int(hexa_num, 16)
        nums.add(tmp)
        
    ans = sorted(list(nums), reverse=True)[k-1]
    
    print(f"#{case} {ans}")
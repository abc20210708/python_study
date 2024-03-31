## 좌표 압축(실버 2)
#  참고 블로그 https://velog.io/@zinu/%EB%B0%B1%EC%A4%80-18870-%EC%A2%8C%ED%91%9C-%EC%95%95%EC%B6%95%ED%8C%8C%EC%9D%B4%EC%8D%AC

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
# 입력받은 좌표들을 중복을 제거하기 위해 set형으로 바꿔주기
s = sorted(set(nums))

# dic = {s[i]:i for i in range(len(s))}
dic = {}

for i in range(len(s)):
    dic[s[i]] = i

for i in nums:
    print(dic[i], end=" ")
    

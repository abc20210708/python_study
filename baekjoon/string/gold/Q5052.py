## 전화번호 목록 (골드 4) *

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = [input().strip() for _ in range(n)]
    arr.sort()
    check = "yes"
    
    # 반복문을 통해 전화번호 확인
    for i in range(len(arr) -1):
        # 현재 전화번호의 문자열과 다음 전화번호의
        # 현재 전화번호 길이만큼의 문자열과 같은지 확인
        # 같으면 일관성이 없는 것
        if arr[i] == arr[i+1][0:len(arr[i])]:
            print(arr[i+1][0:len(arr[i])])
            print(arr[i+1])
            print(arr[0:len(arr[i])])
            check = "no"
    if check == "no":
        print("NO")
    else:
        print("YES")        
    
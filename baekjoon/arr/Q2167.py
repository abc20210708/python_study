## 스택 수열 (실버 2) *
# 참고 블로그 https://velog.io/@ny_/%EB%B0%B1%EC%A4%80-1874%EB%B2%88.-%EC%8A%A4%ED%83%9D-%EC%88%98%EC%97%B4-%ED%8C%8C%EC%9D%B4%EC%8D%AC

import sys

cnt = 1
tmp = True
stack = []
res = []

n = int(sys.stdin.readline())
for i in range(n):
    num = int(sys.stdin.readline())
    # num 이하 숫자까지 스택에 넣기
    while cnt <= num:
        stack.append(cnt)
        res.append("+")
        cnt += 1
    
    # num이랑 스택 맨 위 숫자가 동일하다면 제거
    if stack[-1] == num:
        stack.pop()
        res.append("-")
    # 스택 수열 만들 수 없으므로 NO
    else:
        tmp = False
        break
    
# 스택 수열을 만들수 있는지 여부에 따라 출력
if not tmp:
    print("NO")
else:
    print("\n".join(res))
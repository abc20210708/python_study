## N과 M(1) - (실버 3)
#  참고 블로그 https://jie0025.tistory.com/455

import sys
input = sys.stdin.readline

def backtracking():
    if len(arr) == m:
        print(" ".join(map(str, arr)))
        return
    
    for i in range(1, n+1):
        if i not in arr:
            arr.append(i) # 자식 이동
            backtracking() # 재귀
            arr.pop() # 부모로 이동
    

n, m = map(int, input().split())
arr = []

backtracking()
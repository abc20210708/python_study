## 간판 (실버 5) *

'''
name이 각 입력 문자열(s)의 부분 문자열로 존재하는지
확인하고 그 개수를 세는 문제


'''

import sys
input = sys.stdin.readline

def solution(a, b, name):
    for i in a:
        for j in [k for k in b if i < k]:
            step = j - i
            if name in s[i::step]:
                print(s[i::step])
                return 1
    return 0 

n = int(input())
name = input().rstrip()
cnt = 0

for _ in range(n):
    s = input().rstrip()
    start = [i for i in range(len(s)) if s[i] == name[0]]
    second = [i for i in range(len(s)) if s[i] == name[1]]
    cnt += solution(start, second, name)

print(cnt)

'''
solution 함수에서, 문자열에서 name이 존재하는지 확인하는 부분입니다. 
solution 함수는 name의 첫번째 글자와 두번째 글자가 등장하는 위치를 
start와 second 리스트에 저장하고, 
이를 이용하여 문자열에서 name이 존재하는지 확인합니다. 

이를 위해 step 변수를 이용하여 문자열을 점프하며, 
s[i::step]은 i부터 시작하여 step 간격으로 문자열을 
가져오는 것을 의미합니다. 

예를 들어, s = "hello", i = 1, step = 2일 때, 
s[i::step]은 "el"이 됩니다. 
이를 이용하여 각 위치에서 name이 존재하는지 확인할 수 있습니다.
'''
## 간판 (실버 5) *

'''
name이 각 입력 문자열(s)의 부분 문자열로 존재하는지
확인하고 그 개수를 세는 문제


'''

import sys
input = sys.stdin.readline

def solution(start, second, name):
    # 시작 위치와 두 번째 위치를 이용하여 새 간판을 만들 수 있는가
    for i in start:
        for j in [k for k in second if i < k]:
            step = j - i
            # 일정한 간격으로 문자열을 확인해 새 간판을 만들 수 있는지
            if name in s[i::step]:
                print(s[i::step])
                return 1 # 새 간판을 만들 수 있는 경우 1 반환
    return 0  # 새 간판을 만들 수 없는 경우 0 반환

n = int(input())
name = input().rstrip()
cnt = 0 # 상근이가 만들 수 있는 간판의 수를 세는 변수

for _ in range(n):
    s = input().rstrip()
    # 첫 번째 문자의 위치 찾기
    start = [i for i in range(len(s)) if s[i] == name[0]]
    # 두 번째 문자의 위치 찾기
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
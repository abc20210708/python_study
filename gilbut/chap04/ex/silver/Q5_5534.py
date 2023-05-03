## 간판 (실버 5) *

'''
name이 각 입력 문자열(s)의 부분 문자열로 존재하는지
확인하고 그 개수를 세는 문제

# 참고 블로그 http://mrk0607.tistory.com/1336
'''

# sol 함수는 old_name에서 target을 추출하여 target과 일치하는 경우 1을 반환하고, 
# 그렇지 않은 경우 0을 반환합니다.
def sol(s, target):
    # old_name의 길이를 저장합니다.
    l = len(old_name)
    # old_name에서 문자열을 추출할 시작 위치를 결정합니다.
    for start in range(l):
        # 추출한 문자열의 첫 문자와 target의 첫 문자가 
        # 같은 경우에만 계속 진행합니다.
        if s[start] == target[0]:
            # 추출한 문자열의 끝 위치를 결정합니다.
            for end in range(start, l):
                # 추출한 문자열의 마지막 문자와 target의 마지막 문자가
                # 같은 경우에만 계속 진행합니다.
                if s[end] == target[-1]:
                    # 문자열 추출 간격을 계산합니다.
                    gap = (end - start) // (len(target) - 1)
                    i = 0
                    # 추출한 문자열과 target의 각 문자를 비교합니다.
                    while i < len(target):
                        if s[start + i * gap] == target[i]:
                            i += 1
                        # 문자열이 일치하지 않는 경우, 비교를 중단합니다.
                        elif s[start + i * gap] != target[i]:
                            break
                    # 문자열이 일치하는 경우 1을 반환합니다.
                    else:
                        return 1
    # 문자열이 일치하지 않는 경우 0을 반환합니다.
    return 0


# 입력받는 편의점 이름의 길이와 내용을 저장합니다.
n = int(input())
name = input()
res = 0
# 각 오래된 간판을 입력받아서 sol 함수를 호출하여 결과를 합산합니다.
for _ in range(n):
    old_name = input()
    res += sol(old_name, name)
# 가능한 새 간판의 수를 출력합니다.
print(res)

'''
while 문은 break 문을 만나지 않고 끝까지 실행되면 else 블록 내의 코드가 실행됩니다. 
이는 Python의 특별한 구문으로서, while 루프가 완전히 실행된 경우에만 실행됩니다. 
즉, while 루프가 break 문에 의해 중간에 종료되면 else 블록이 실행되지 않습니다.

따라서, while 루프가 끝까지 실행되고 target과 추출한 문자열이 일치하는 경우에만 
return 1이 실행되어 1을 반환합니다. 

이는 sol 함수에서 추출한 문자열과 target 문자열이 일치하는 경우,
1을 반환하여 가능한 새 간판의 수를 1 증가시키는데 사용됩니다.
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
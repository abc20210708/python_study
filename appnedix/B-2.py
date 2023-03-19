# 암호 만들기

'''
4,6
a t c i s w
'''

from itertools import combinations

d = ('a', 'e', 'i', 'o', 'u') # 5개의 모음 정의
l, c = map(int, input().split())

# 가능한 암호를 사전식으로 출력해야 하므로 입력 이후에 정렬 수행
arr = input().split()
arr.sort()

# 길이가 1인 모든 암호 조합을 확인
for password in combinations(arr, l):
    # 패스워드에 포함된 각 문자를 확인하며 모음의 개수를 세기
    cnt = 0
    for i in password:
        if i in d:
            cnt += 1
    # 최소 1개의 모음과 최소 2개의 자음이 있는 경우 출력
    if cnt >= 1 and cnt <= l -2:
        print(''.join(password))
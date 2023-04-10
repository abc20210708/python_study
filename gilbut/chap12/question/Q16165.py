# 걸그룹 마스터 준석이 (실버 3) *

# 참고 블로그 https://chancoding.tistory.com/74
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dic1, dic2 = {}, {}

for _ in range(n):
    team = input().rstrip()
    members = []
    for i in range(int(input())):
        name = input().rstrip()
        dic1[name] = team
        members.append(name)
    dic2[team] = members

for _ in range(m):
    target = input().rstrip()
    num = int(input())
    if num == 1:
        print(dic1[target])
    else:
        mem = dic2[target]
        print('\n'.join(sorted(mem)))


## 타노스 (실버 3)

'''
간단하게 그리디로 접근 가능한 문제이다. 
잘 생각해보면 같은 위치의 1, 0 중 0이 
사전적으로 앞서므로 0은 가급적 앞에, 
1은 가급적 뒤에 남아 있는게 좋다. 

즉 0은 오른쪽부터 왼쪽으로 탐색하며 절반을 제거하고, 
1은 왼쪽부터 오른쪽으로 탐색하며 절반을 제거하면 
사전순으로 가장 앞서는 문자열을 남길 수 있다.
'''

# 다른 풀이
# 참고 블로그 https://magentino.tistory.com/231
import sys
input = sys.stdin.readline

s = list(input().rstrip())
length = len(s)

one = s.count('1') // 2
zero = s.count('0') // 2

idx = len(s) - 1
while zero :
    if s[idx] == '0' :
        s.pop(idx)
        zero -= 1
    idx -= 1

idx = 0
while one :
    if s[idx] == '1' :
        s.pop(idx)
        one -= 1
    else :
        idx += 1

print(''.join(s))




#  참고 블로그 https://velog.io/@peacemiller/%EB%B0%B1%EC%A4%80-20310-%ED%83%80%EB%85%B8%EC%8A%A4-python



s = list(input().rstrip())

zero = s.count('0')
one = s.count('1')

# 앞에서부터 1을 갯수의 절반 만큼 지우고
# 뒤에서부터 0을 갯수의 절반 만큼 지우자

cnt = 0
for i in s:
    if cnt == one//2:
        break
    if i == '1':
        s.remove(i)
        cnt += 1


tmp = 0
s = s[::-1]
for i in s:
    if tmp == zero//2:
        break
    if i == '0':
        s.remove(i)
        tmp += 1

s = s[::-1]
print(''.join(s))

#for i in s[::-1]:
#    print(i, end='')
## 타노스 (실버 3)

# 다른 풀이
# 참고 코드 https://www.acmicpc.net/source/68673596
import sys
input = sys.stdin.readline

s = list(input().rstrip())
length = len(s)

one = s.count('1') // 2
zero = s.count('0') // 4

for x in range(length)[::-1]:
    if s[x] == '0' and zero:
        s[x] = ''
        zero -= 1

for x in range(length):
    if s[x] == '1' and one:
        s[x] = ''
        one -= 1

print("".join(s))




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
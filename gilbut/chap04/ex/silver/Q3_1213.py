## 팰린드롬 만들기 (실버 3) *

import collections
import sys

# 참고 블로그 https://velog.io/@rovna/%EB%B0%B1%EC%A4%80-1213%EB%B2%88-%ED%8C%B0%EB%A6%B0%EB%93%9C%EB%A1%AC-%EB%A7%8C%EB%93%A4%EA%B8%B0
# 참고 블로그 https://fre2-dom.tistory.com/310
#input = "ABACABA"
input = sys.stdin.readline
word = input().rstrip()
chk_word = collections.Counter(word)
cnt = 0

res = ""
mid = ""

for k,v in list(chk_word.items()):
    if v % 2 == 1: 
        cnt += 1
        mid = k
        if cnt >= 2: # 홀수가 2개 이상이면 팰린드롬이 X
            print("I'm Sorry Hansoo")
            exit()
            
for k, v in sorted(chk_word.items()):
    res += (k * (v // 2))
print(res + mid + res[::-1])

'''
코드에서 break 대신 exit() 함수를 사용하는 이유는 
break는 내부 루프에서만 빠져나오고 나머지 코드는 
계속 실행되는 반면, exit()는 프로그램을 즉시 종료시킵니다. 

이 경우, 입력된 문자열이 회문으로 재배열될 수 없다는 것이 
결정되면 나머지 코드를 계속 실행할 필요가 없기 때문에 
exit() 함수를 사용하여 프로그램을 종료하고 
"I'm Sorry Hansoo" 메시지를 출력합니다.
'''

s = list(map(str, sys.stdin.readline().strip()))
s.sort()
check = collections.Counter(s)

count = 0
center = ""

for i in check:
    if check[i] % 2 == 1:
        count += 1
        center += i
        s.remove(i)
    if count > 1: break

if count > 1:
    print("I'm Sorry Hansoo")
else:
    result = ""
    for i in range(0, len(s), 2):
        result += s[i]
    print(result + center + result[::-1])
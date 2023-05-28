## 에디터 (실버 2) *
# 참고 코드 https://www.acmicpc.net/submit/1406/61395524

from sys import stdin

st1 = list(stdin.readline().rstrip())
st2 = []

for _ in range(int(input())):  # 입력 횟수(n)만큼 반복합니다.
    i = stdin.readline().rstrip()  # 표준 입력에서 한 줄씩 입력을 받아옵니다.

    if i[0] == 'L':
        if st1:
            st2.append(st1.pop())
        else:
            continue
    elif i[0] == 'D':
        if st2:
            st1.append(st2.pop())
        else:
            continue
    elif i[0] == 'B':
        if st1:
            st1.pop()
        else:
            continue
    elif i[0] == 'P':
        st1.append(i[2])

print(''.join(st1 + list(reversed(st2))))
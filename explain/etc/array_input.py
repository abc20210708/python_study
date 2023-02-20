## 참고 블로그 https://covenant.tistory.com/141


'''
3
1 2 3
4 5 6
7 8 9

첫 번째 줄에는 입력되는 숫자들의 줄 수가 주어지며,
다음 줄부터는 숫자들이 공백을 기준으로 주어집니다.
'''

# 2-1. 우아한 배열 입력
ARR = [list(map(int, input().split())) for _ in range(int(input()))]

# 2-2. 정수와 배열이 같은 줄에 들어오는 경우
'''
백준 9613에서 사용할 수 있는 코드
한 줄에는 수의 개수 n이 주어지고, 다음에는 n개의 개수가 주어진다.
이 때의 입력을 어떻게 구현할까

4 10 20 30 40
3 7 5 12
3 125 15 25
'''

# arr 변수 앞에 *를 분이면 뒤이어 나오는 값이
# arr에 배열로 저장이 된다.
N, *arr = map(int, input().split())


# 2-3. 문자열을 한 글자씩 배열에 저장

'''
문자열을 한 글자씩 배열에 저장을 해야할 때

3
AAAA
ABCA
AAAA

arr = [['A', 'A', 'A', 'A']
       ['A', 'B', 'C', 'A']
       ['A', 'A', 'A', 'A']]
'''

# 잘못된 예
# word = [input() for _ in range(N)]
# 결과 arr = ['AAAA', 'ABCA', 'AAAA']

# 목표를 이루기 위해 list(input())
# list를 input 앞에 붙이면 입력받은 문자열을
# 글자로 잘라서 저장
word = [list(input()) for _ in range(N)]


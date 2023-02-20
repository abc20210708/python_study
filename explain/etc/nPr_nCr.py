## 참고 블로그 https://covenant.tistory.com/143

# 1. 순열, 조합

# 1-1. 순수한 방법
# for문 2개를 사용해 nC2를 구하는 방법
P =3
for i in range(0, P-1):
    for j in range(i + 1, P):
        print(i, j)
        
        
# 1-2. itertools를 사용한 조합
from itertools import combinations
print(list(combinations([1, 2, 3, 4], 3)))

'''
combinations의 첫 번째 인자에 배열을 넣고, 
두 번째 인자에는 nCm 이라면 m에 해당하는 값을 넣습니다. 
출력 결과는 다음과 같습니다.

# [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]
'''

'''
백준 15650번 N과 M (2) 문제를 풀어보겠습니다. 
N과 M의 숫자가 주어졌을 때 다음 조건을 만족해야 합니다.

- 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
- 고른 수열은 오름차순이어야 한다.
'''

from itertools import combinations

N, M = map(int, input().split())
# 1부터 N까지의 수를 arr에 저장
arr = [str(i + 1) for i in range(N)]

for k in list(combinations(arr, M)):
    print(" ".join(k))
    
    
# 1-3 순열
'''
백준 15649번 N과 M (1) 문제를 살펴보겠습니다.
- 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
'''
from itertools import permutations

I, J = map(int, input().split())
arr1 = [str(i+1) for i in range(I)]

for i in list(permutations(arr, J)):
    print(" ".join(i))

# 1-4 중복 순열과 중복 조합

# 중복 순열
from itertools import product
# 중복 조합
from itertools import combinations_with_replacement


# 2. 빈도 계산
from collections import Counter

arr2 = [int(input()) for _ in range(10)]
val = Counter(arr2).most_common()
print(sum(arr) // 10)
print(val[0][0])


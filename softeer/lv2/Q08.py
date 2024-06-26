# 바이러스

import sys

'''
문제
바이러스가 숙주의 몸속에서 1초당 P배씩 증가한다.



처음에 바이러스 K마리가 있었다면 N초 후에는 
총 몇 마리의 바이러스로 불어날까? 
N초 동안 죽는 바이러스는 없다고 가정한다.

제약조건
1 ≤ K ≤ 108인 정수

1 ≤ P ≤ 108인 정수

1 ≤ N ≤ 106인 정수

입력형식
첫 번째 줄에 처음 바이러스의 수 K, 
증가율 P, 총 시간 N(초)이 주어진다.

입력예제1
2 3 2
출력예제1
18
'''

input = sys.stdin.readline


### 다른 풀이 
#   참고 블로그 https://velog.io/@charbs0701/python-%EC%86%8C%ED%94%84%ED%8B%B0%EC%96%B4-%EB%B0%94%EC%9D%B4%EB%9F%AC%EC%8A%A4
virus, rate, n = map(int, input().split())

for i in range(n):
    virus = virus * rate
    virus = virus % 1000000007


print(virus % 1000000007)


#k, p, n = map(int, input().split())
k, p, n = 2, 3, 2

# 출력 형식 : 최종 바이러스 개수를 
# 1000000007로 나눈 나머지를 출력하라.

# pow() 계산시 mod값 설정을 하여 시간단축을 시킨 후 
# K를 곱한 값이 1e9+7 을 넘어갈 수 있기 때문에 
# 한번더 1e9+7로 나눈 나머지 값을 구한다
#print(k * pow(p, n) % int(1e9 + 7) % int(1e9 + 7))

#print(k * pow(p, n, int(1e9+7)) % int(1e9+7))

print((k * pow(p, n, 1000000007)) % 1000000007)

'''
참고 블로그 https://hwisaek.tistory.com/entry/Softeer-%EB%B0%94%EC%9D%B4%EB%9F%AC%EC%8A%A4-Python

제곱을 그대로 하게 된다면 숫자가 기하급수적으로 증가해
다른 언어로 한다면 데이터의 범위를 벗어날 수도 있고,
연산하는데 엄청난 시간을 소모하게 된다.

pow(base, exp, mod)를 이용해야 합니다. pow라는 함수는
base를 exp 제곱하는 함수인데, mod 파라미터를 이용하게 된다면
거듭제곱을 수행하면서 숫자가 커지면 나머지 연산을 수행하여
효율적으로 계산할 수 있다.
'''
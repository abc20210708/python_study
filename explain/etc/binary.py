## 참고 블로그 https://covenant.tistory.com/142

# 2-1  10진수 -> 2, 8, 16
print(bin(42))
print(oct(42))
print(hex(42))

# 2-2 16진수 -> 10진수 변환
print(int('0b111100', 2))
print(int('0o74', 8))
print(int('0x3c', 16))

# 2-3 진법 연산 예제
'''
3
1001101 10010
1001001 11001
1000111 1010110

백준 2729번 첫 줄에는 테스트 케이스의 수가 주어지며
테이스 케이스 줄 수 만큼 2진수가 2개 주어진다고 했을 때
각 이진수의 합을 구하라는 문제
'''

# 일단 int로 입력 받아 bin()로 변환하고 바로 덧셈 연산
# 그러면 이진수 연산이 이루어짐

for _ in range(int(input())):
    A, B = map(int, input().split())
    print(bin(A) + bin(B))
## 가장 긴 증가하는 부분 수열 (실버 2)
#  참고 블로그 https://velog.io/@djagmlrhks3/Algorithm-BaekJoon-11053.-%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4-by-Python
#  https://duckracoon.tistory.com/entry/%EB%B0%B1%EC%A4%80-11053-%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4-%ED%95%B4%EC%84%A4-python


# 다른 풀이
# 참고 블로그 https://yjg-lab.tistory.com/409
import sys
input = sys.stdin.readline

# 길이를 입력
n = int(input())

arr = list(map(int, input().split()))

# 각 숫자를 마지막 원소로 가지는 증가하는 부분 수열의
# 최대 길이를 저장하는 리스트를 생성합니다.
# 이때, 각 숫자는 0 이상이므로, table 리스트의 길이를 
# 수열의 최대값보다 크게 설정합니다.
table = [0] * (max(arr) + 1)

# 입력받은 수열을 순회하면서 각 숫자를 마지막 원소로 
# 가지는 부분 수열의 길이를 구합니다.
for v in arr:
    # 현재 숫자를 마지막 원소로 가지는 부분 수열 중, 
    # 그 원소보다 작은 숫자들로 구성된 부분 수열의 길이 중 최대값을 찾습니다.
    # table 리스트는 이전에 계산한 부분 수열의 길이를 저장하고 있으므로,
    # 0부터 현재 숫자 직전까지의 인덱스 범위를 확인합니다.
    # 이때, 해당 인덱스의 값을 모두 비교하고 그 중 가장 큰 값에 1을 더한 값이 
    # 현재 숫자를 마지막으로 하는 부분 수열의 길이가 됩니다.
    # 따라서 table 리스트의 해당 인덱스에 현재 부분 수열의 길이를 저장합니다.
    table[v] = max(table[:v]) + 1

# table 리스트에서 가장 큰 값이 가장 긴 증가하는 부분 수열의 길이가 됩니다.
# 이 값을 출력합니다.
print(max(table))

'''
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
'''
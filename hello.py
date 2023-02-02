
# 큰 수의 법칙 다시 풀어보기

'''
다양한 수로 이루어진 배열이 있을 때 주어진 수들을
M번 더하여 가장 큰 수를 만드는 법칙
단, 배열의 특정한 인덱스(번호)에 해당하는 수가
연속해서 K번을 초과해 더해질 수 없는 것이 이 법칙의 특징
'''

n, m, k = 5, 7, 2
data = [3, 4, 3, 4, 3]

data.sort()

first = data[-1]
second = data[-2]

result = 0

cnt = (m // (k+1)) * k
cnt += m % (k + 1)

result = (cnt) * first
result += (m - cnt) * second

print(result)






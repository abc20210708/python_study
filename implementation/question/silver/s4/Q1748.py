## 수 이어 쓰기 1 (실버 4)
#  참고 블로그 https://gudwns1243.tistory.com/24

n = input()
res = 0

tmp = len(n) - 1

for i in range(tmp):
    res += 9 *(10 ** i) * (i + 1)
    i += 1
res += ((int(n) - (10 ** tmp)) + 1) * (tmp + 1)

print(res)

## 규칙성
'''
주어진 숫자의 자릿수보다 하나 적은 자릿수의 수는 9 * (10) ^ (n-1)개 
여기에 각 자릿수를 곱하면 되는 규칙이 있었다.

즉, 9 * (10) ^ (n-1) * n 의 규칙을 따른다.
'''
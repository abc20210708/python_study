## 피보나치 함수 (실버 3)

zero = [1, 0, 1, 1, 2]
one = [0, 1, 1, 2, 3]

# N이 주어진다. N은 40보다 작거나 같은 자연수 또는 0

for i in range(5, 41):
    zero.append(zero[i-1]+ zero[i-2])
    one.append(one[i-1]+ one[i-2])
    


for _ in range(int(input())):
    n = int(input())
    print(zero[n], one[n])
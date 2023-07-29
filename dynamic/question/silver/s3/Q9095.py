## 1, 2, 3 더하기 (실버 3) *
# 참고 블로그 https://e-you.tistory.com/304
d = [0] * 11
d[1] = 1
d[2] = 2
d[3] = 4

# d 리스트는 1, 2, 3을 이용해 만들 수 있는 모든 수의 경우의 수를 저장합니다.
# d[1]은 1을 만들 수 있는 경우의 수, d[2]는 2를 만들 수 있는 경우의 수, d[3]은 3을 만들 수 있는 경우의 수입니다.
# 문제에서 주어진 대로 초기값을 설정해 줍니다.

for i in range(4, 11):
    # 4부터 10까지의 수에 대해 경우의 수를 구합니다.
    # i - 3, i - 2, i - 1의 경우의 수를 더해서 d[i]에 저장합니다.
    # 예를 들어, d[4]는 d[1] + d[2] + d[3]으로 구할 수 있습니다.
    d[i] = d[i - 3] + d[i - 2] + d[i - 1]

n = int(input())
for _ in range(n):
    m = int(input())
    # n을 입력받고, n개의 수에 대해 경우의 수를 출력합니다.
    # m을 입력받아 d[m]을 출력합니다.
    print(d[m])
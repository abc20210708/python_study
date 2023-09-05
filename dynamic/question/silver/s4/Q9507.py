## Generations of Tribbles (실버 4)

d = [1] * 68
d[2] = 2
d[3] = 4
for i in range(4, 68):
    d[i] = d[i-1] + d[i-2] + d[i-3] + d[i-4]

for _ in range(int(input())):
    print(d[(int(input()))])
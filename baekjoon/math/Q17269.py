# 이름궁합 테스트

import string

alp_list = list(string.ascii_uppercase)
cnt_list = [3,2,1,2,4,3,1,3,1,1,3,1,3,2,1,2,2,2,1,2,1,1,1,2,2,1]
alpha_count = dict()
x = 0

for a in alp_list:
    alp_list[a] = cnt_list[x]
    x += 1
    
n, m = map(int, input().split())
a, b = map(int, input().split())
i, j = 0, 0
c = []

while i <= len(a) or j <= len(b):
    if i < len(a):
        c.append(alpha_count[a[i]])
    if j < len(b):
        c.append(alpha_count[b[j]])
    i += 1
    j += 1
    
while len(c) > 2:
    c1 = c.pop(0)
    for x in range(len(c)):
        c2 = c.pop(0)
        c.append((c1+c2)%10)
        c1 = c2

print("%s%%" % str(c[0]*10+c[1]))

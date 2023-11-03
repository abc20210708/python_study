## 생태학 (실버 2)
#  참고 블로그 https://imzzan.tistory.com/29

dic = dict()

total = 0
while 1:
    s = input().rstrip()

    if s == '':
        break
    total += 1
    if s not in dic:
        dic[s] = 1
    else:
        dic[s] += 1
    
tmp = dict(sorted(dic.items()))

for i in tmp:
    a = tmp[i]
    num = (a / total * 100)
    print("%s %.4f" %(i, num))  
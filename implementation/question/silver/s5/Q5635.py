## 생일 (실버 5)

t = int(input())
dic = dict()    

for _ in range(t):
    name, day, month, year = map(str, input().split())
    if int(month) < 10:
        month = "0" + month
    elif int(day) < 10:
        day = "0" + day
    dic[name] = (year + month + day)
    
tmp = list(dict(sorted(dic.items(), key=lambda x:x[1])))

print(tmp[-1])
print(tmp[0])



# 잃어버린 괄호

## 참고 블로그 https://sungmin-joo.tistory.com/67

s = "55-50+40".split("-")

num = 0

for i in s[0].split("+"):
    num += int(i)
for i in s[1:]:
    for j in i.split("+"):
        num -= int(j)
        
print(num)
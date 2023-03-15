# 잃어버린 괄호

## 참고 블로그 https://sungmin-joo.tistory.com/67

# "55-(50+40)" 결과의 최소

s = "55-50+40".split("-") # 입력 받은 수식을 '-'로 나눕니다.
# 첫 번째 부분식은 그대로 더합니다.
res = sum(map(int, s[0].split("+")))

for i in s[1:]: # 나머지 부분식에 대해서
    res -= sum(map(int, i.split("+"))) # 빼줍니다.
    
print(res)

'''
s = "55-50+40".split("-")

num = 0

for i in s[0].split("+"):
    num += int(i)
for i in s[1:]:
    for j in i.split("+"):
        num -= int(j)
        
print(num)
'''
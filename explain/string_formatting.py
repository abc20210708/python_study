
# f 문자열 포맷팅
name = "홍길둉"
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')
print(f'나는 내년이면 {age + 1}살이 됩니다.')




## format 함수를 사용한 포매팅

# 1. 숫라 바로 대입하기
print("I eat {0} apples".format(9))

# 2. 문자열 바로 대입하기
print("I eat {0} apples".format("seven"))

# 3. 숫자 값을 가진 변수로 대입하기
n = 6
print("I eat {0} apples".format(n))

# 4. 2개 이상의 값 넣기
i = 11
d = "four"
print("I eat {0} apples. so I was sick for {1} days".format(i, d))

# 5. 이름으로 넣기
print("I eat {j} apples. so I was sick for {k} days".format(j = 20, k = 5))

# 6. 인뎃르와 이름 혼용해서 넣기
print("I eat {0} apples. so I was sick for {m} days".format(28, m = 8))




## 문자열 포멧팅

# 1. 숫자 바로 대입

print("I eat %d apples." % 3)

# 2. 문자열 바로 대입
print("I eat %s apples." % "five")

# 3. 숫자 값을 나타내는 변수로 대입
num = 3
print("I eat %d apples." % num)

# 4. 2개 이상의 값 넣기
number = 10
day = "three"
print("I ate %d apples. so I was sick for %s days" %(number, day))

####

print("{0:<10}".format("hi")) # 왼쪽 정렬 
print("{0:>10}".format("hi")) # 오른쪽 정렬 
print("{0:^10}".format("hi")) # 가운데 정렬 

print("{0:=^10}".format("hi")) # 공백 채우기 
print("{0:!<10}".format("hi")) # 공백 채우기 

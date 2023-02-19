
# 문자열 관련 함수

# count 문자 개수 세기
a = "hobby"
print(a.count('b'))

# find 위치 알려주기
b = "Python is the best choice"
print(b.find('b')) # 문자열에서 b가 처음 나온 위치
print(b.find('k')) # 존재하지 않는다면 -1을 반환

# index 위치 알려주기
c = "Life is too short"
print(c.index('t'))
#print(c.find('k')) # find 함수와는 다르게 없으면 오류

# join 문자열 삽입
print(",".join("abcd"))
print(" ".join(["a", "b", "c", "d"]))

# upper 소문자를 대문자로 바꾸기
d = "hi"
print(d.upper())

# lower 대문자를 소문자로 바꾸기
e = "HI"
print(e.lower())

# lstrip 왼쪽 공백 지우기
f = "  hi  "
print(f.lstrip())

# rstip 오른쪽 공백 지우기
g = "  HI  "
print(g.rstrip())

# strip 양쪽 공백 지우기
h = "  hh  "
print(h.strip())

# replace 문자열 바꾸기
i = "Life is too short"
print(i.replace("Life", "Your leg"))

# split 문자열 나누기
j = "Life is too short"
print(j.split()) # 공백을 기준으로 문자열을 나눔
k = "a:b:c:d"
print(k.split(":"))
## strip
#  참고 블로그 https://buyandpray.tistory.com/48


s = "aaaaabbbbbbaaaaa"
# 특정 문자 제거
# 해당 문자가 나오지 않을 때까지 제거

# 양쪽에서 a가 나오지 않을 때까지 제거
# bbbbbb
s1 = s.strip("a")
print(s1)

# 왼쪽에서 a가 나오지 않을 때까지 제거
# bbbbbbaaaaa
s.lstrip("a")

# 오른쪽에서 a가 나오지 않을 때까지 제거
# aaaaabbbbbb
s.rstrip("a")

# 양쪽에서 a또는 b가 나오지 않을 때까지 제거
# a 또는 b를 제거하기 때문에 공백이 출력된다.
# 공백출력
print(s.strip("ab"))
 
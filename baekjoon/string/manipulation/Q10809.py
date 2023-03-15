# 알파벳 찾기
# 97 122
#s = "baekjoon"
s = input()
arr = [-1] * 26

for i in s:
    arr[ord(i)-97] = s.find(i)
    
for i in arr:
    print(i, end=" ")
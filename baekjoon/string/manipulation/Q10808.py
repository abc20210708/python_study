# 알파벳 개수

#s = "baekjoon"
s = input()
arr = [0] * 26

for i in s:
    arr[ord(i)-97] = s.count(i)
    
for i in arr:
    print(i, end=" ")
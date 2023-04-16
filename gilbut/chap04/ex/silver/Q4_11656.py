## 접미사 배열 (실버 4)

#s = "baekjoon"
s = input()
arr = []

for i in range(len(s)):
    arr.append(s[i:])
    
arr.sort()

for i in arr:
    print(i)
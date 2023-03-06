# 단어 공부
## 참고 블로그 https://velog.io/@beaver-zip/1157%EB%B2%88-%EB%8B%A8%EC%96%B4-%EA%B3%B5%EB%B6%80-Python
word = "Mississipi".upper()
cnt = 0

for i in set(word):
    if word.count(i) > cnt:
        temp = i
        cnt = word.count(i)
    elif word.count(i) == cnt:
        temp = "?"

print(temp)
'''
word = input().upper()

arr = [0] * 26

for i in word:
    arr[ord(i) - 65] += 1

sum_val = max(arr)
cnt = 0

for i in arr:
    if cnt > 1: break
    if i == sum_val:
        cnt += 1
    
if cnt > 1:
    print("?")
else:
    print(chr(arr.index(sum_val)+65))
'''
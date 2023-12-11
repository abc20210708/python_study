## 모음의 개수 (브론즈 3)
#  단어의 길이는 1보다 크거나 같고
#  100보다 작거나 같으며 알파벳 소문자로만 이루어짐

s = input()
target = ['a', 'e', 'i', 'o', 'u']
cnt = 0

for i in s:
    if i in target:
        cnt += 1

print(cnt)
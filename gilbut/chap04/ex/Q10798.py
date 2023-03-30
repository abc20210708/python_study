## 세로읽기 (브론즈 1) *

# 참고 블로그 https://v-0w0-v.tistory.com/entry/Python-%EB%B0%B1%EC%A4%80-10798-%EC%84%B8%EB%A1%9C%EC%9D%BD%EA%B8%B0-2%EC%B0%A8%EC%9B%90-%EB%B0%B0%EC%97%B4
arr = []
res = ''

for i in range(5):
    arr.append(input())

for i in range(15):
    for j in range(5):
        if i < len(arr[j]):
            res += arr[j][i]
    
print(res)


words = []
max_len = 0

# 입력받은 5개의 문자열을 리스트에 저장하고
# 가장 긴 문자열의 길이를 구하기
for i in range(5):
    word = input()
    words.append(word)
    max_len = max(max_len, len(word))
    
# 각 문자열의 n번째 문자열 세로로 출력
for i in range(max_len):
    for j in range(5):
        if i < len(words[j]):
            print(words[j][i], end="")
        else:
            continue
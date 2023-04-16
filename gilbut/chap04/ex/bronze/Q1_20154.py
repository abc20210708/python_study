## 이 구역의 승자는 누구야? (브론즈 1)*

alpha = [3,2,1,2,3,3,3,3,1,1,3,1,3,3,1,2,2,2,1,2,1,1,2,2,2,1]

#s = input()
s = "ABCDE"
arr = []
for a in s:
    i = ord(a) - ord('A')
    arr.append(alpha[i])

res = sum(arr) % 10
if res % 2 == 1:
    print("I'm a winner!")
else:
    print("You're the winner?")
    
# 참고 블로그 https://ssafy-story.tistory.com/72
## 오렌지먹은오렌지 (브론즈 1)
#  참고 블로그 https://velog.io/@yoonkeem/BOJ-27962%EB%B2%88-%EC%98%A4%EB%A0%8C%EC%A7%80%EB%A8%B9%EC%9D%80%EC%A7%80%EC%98%A4%EB%9E%9C%EC%A7%80-%ED%8C%8C%EC%9D%B4%EC%8D%AC
N = int(input())
sent = input()
ans = ""
for i in range(1, N):
    a = sent[:i] # 앞에서부터 1칸씩
    r = sent[::-1]
    b = r[:i][::-1] # 뒤에서부터 1칸씩
    
    check = 0
    for j in range(len(a)):
        if a[j] != b[j]:
            check += 1
    if check == 1: # 단 1개만 다르다면
        ans = "YES"
        break
if ans != "YES":
    ans = "NO"
print(ans)
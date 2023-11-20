## 오늘도 졌다 (실버 5)
#  참고 블로그 https://woojinhong.tistory.com/m/155
#  https://ddo-code.tistory.com/54

w = list(map(int, input().split()))
s = list(map(int, input().split()))

w_sum, s_sum = 0, 0
cnt = 0

for i in range(9):
    w_sum += w[i]
    
    if w_sum > s_sum and cnt == 0:
        cnt += 1
    if w_sum < s_sum and cnt == 1:
        cnt += 1
    s_sum += s[i]
    
if cnt == 2 and w_sum < s_sum or cnt == 1 and w_sum < s_sum:
    print("Yes")
else:
    print("No")

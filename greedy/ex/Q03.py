# 문자열 뒤집기

## 참고 블로그 https://wooono.tistory.com/541
#data = input()
s = "0001100"
cnt0 = 0 # 0이 연속된 부분
cnt1 = 0 # 1이 연속된 부분

# 첫 번째 정수는 곧바로 연속된 부분으로 추가
if s[0] == '0':
    cnt0 += 1
else :
    cnt1 += 1
    
    
# 정수를 순서대로 탐색하며, 
# 연속된 정수가 다른 정수로 바뀔 때, 연속된 부분의 개수 추가
for i in range(len(s) - 1) :
    
    # 연속된 정수가 다음 수에서 다른 정수로 바뀔 때
    if s[i] != s[i + 1]:
        # 다음 수에서 0으로 바뀌는 경우
        if s[i + 1] == '0':
            cnt0 += 1
        # 다음 수에서 1로 바뀌는 경우
        else:
            cnt1 += 1

print(min(cnt0, cnt1))
## 이름 궁합 테스트 (브론즈 1) *

n, m = map(int, input().split())
s1, s2 = input().split()

alp = [3,2,1,2,4,3,1,3,1,1,3,1,3,2,1,2,2,2,1,2,1,1,1,2,2,1]
s = ""
end = min(n, m)

for i in range(end):
    s += s1[i] + s2[i]
s += s1[end:] + s2[end:]

lst = [alp[ord(i)-ord('A')] for i in s]

# 계산 수행 횟수(세로) 
# 마지막에 두 개의 숫자를 남겨야 하므로 N+M-2 만큼 반복
for i in range(n + m -2):
    # 계산 (가로)
    for j in range(n + m -1 -i):
        lst[j] += lst[j+1]
        
# 십의 자리이기 때문에 *10
print("{}%".format(lst[0]%10*10 + lst[1]%10))



# 볼링공 고르기 

# 참고 블로그 https://wooono.tistory.com/543
## 볼링공의 개수 N, 공의 최대 무게 M

'''
1(무게가 1인 공의 개수) X 4(무게가 1보다 큰 공의 개수) = 4
2(무게가 2인 공의 개수) X 2(무게가 2보다 큰 공의 개수) = 4
2(무게가 3인 공의 개수) X 0(무게가 3보다 큰 공의 개수) = 0
'''

n, m = map(int, input().split())
data = list(map(int, input().split()))

# 1부터 10까지 무게를 담을 수 있는 리스트
a = [0] * 11

for x in data:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    a[x] += 1
    
result = 0
# 1부터 m까지 각 무게에 대하여 처리
for i in range(1, m + 1) :
    n -= a[i] # 무게가 i인 볼링공의 개수 (A가 선택할 수 있는 개수) 제외
    result += a[i] * n # B가 선택하는 경우의 수와 곱하기
    
print(result)
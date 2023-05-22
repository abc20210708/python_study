## 1로 만들기 (실버 3) *
# 참고 블로그 https://bio-info.tistory.com/159
# https://jae04099.tistory.com/199


target = int(input())
d = [0] * (target + 1)

## 여기서 if elif else를 사용 X, if만 이용해야 세 연산을 다 거칠 수 있다
for i in range(2, target + 1):
    d[i] = d[i - 1] + 1
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1) ## 1을 더하는 것은 d는 결과가 아닌 
                                    #계산한 횟수를 저장하는 것 이기 때문이다. 
                                    # d[i]에는 더하지 않는 이유는 이미 1을 뺄 때 
                                    # 1을 더해준 이력이 있기 때문이다
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)

print(d[target])
## 슈퍼 마리오 (브론즈 1)
#  참고 블로그 https://my-coding-notes.tistory.com/400

# 버섯의 점수를 처음부터 더해간다.
# 총점 -100의 절댓값이 가장 skwdmf rudnddml chdwjadmf cnrfur
# 단, 절댓값이 같을 경우 더 큰 총점을 출력하라는 조건에 유의
res, score = 0, 0

for i in range(10):
    score += int(input())
    if 100-res >= abs(100-score): # =을 넣어야 절댓값이 같을 시
        res = score               # 최대 총점 출력이 가능
print(res)

## 다른 풀이
#  참고 블로그 https://velog.io/@jajubal/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EB%B0%B1%EC%A4%80-2851-%EC%8A%88%ED%8D%BC%EB%A7%88%EB%A6%AC%EC%98%A4

score = 0
mushrooms = []
for _ in range(10):
    mushrooms.append(int(input()))

for i in range(10):
    ex_score = score
    score += mushrooms[i]
    if score >= 100:
        under = 100 - ex_score
        over = score - 100
        if over <= under:
            print(score)
            break
        else:
            print(ex_score)
            break
else:
    print(score)
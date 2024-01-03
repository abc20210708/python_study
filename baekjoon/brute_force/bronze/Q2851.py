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
## 문제9) 시험 등수 구하기
#  참고 블로그 https://popooly.tistory.com/265?category=1073615

def solution(score):
    
    answer = [1 for _ in range(len(score))]
    
    # score끼리 비교해 작으면 등수 추가
    for i in range(len(score)):
        for j in range(len(score)):
            if score[i] < score[j]:
                answer[i] += 1
    return answer


score2 = [10, 20, 20, 30]
ret2 = solution(score2)

print("solution 함수의 반환 값은", ret2, "입니다.")
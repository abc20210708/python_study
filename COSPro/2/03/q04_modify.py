## 문제4) 단어의 오타 수정하기
#  참고 블로그 https://popooly.tistory.com/231

# 풀이 1
def solution1(words, word):
    cnt = 0
    
    # word의 원소들의 문자를 word의 문자와 비교
    for x in words:
        for j in range(len(word)):
            if x[j] != word[j]:
                cnt += 1
    return cnt

# 풀이 2
def solution2(words, word):
    cnt = 0
    
    for tmp in words:
        # zip: tmp, word의 각 문자를 x, y 순서대로 할당
        for x,y in zip(tmp, word):
            if x != y:
                cnt += 1
    
    return cnt 

print(solution2(["CODE", "COED", "CDEO"], "CODE"))
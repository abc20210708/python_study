## 문제1) 사전에서 단어찾기
#  참고 블로그 https://iwantbaobab.tistory.com/57
def create_words(lev, s):
    global words #전역 변수
    VOWELS = ['A', 'E', 'I', 'O', 'U']
    words.append(s)
    for i in range(0, 5):
        if lev < 5:
            create_words(lev+1, s+VOWELS[i])

def solution(word):
    global words # 전역 변수 선언
    words = []
    res = 0
    create_words(0, '')
    
    for idx, i in enumerate(words): 
        if word == i: # 단어와 words를 순회하는 i가 동일한 경우
            res = idx # i의 위치, idx를 저장
            break
    return res

word1 = "AAAAE"
ret1 = solution(word1)

print("solution 함수의 반환 값은", ret1, "입니다.")

word2 = "AAAE"
ret2 = solution(word2)

print("solution 함수의 반환 값은", ret2, "입니다.")
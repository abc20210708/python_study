## 모음 사전 *

# 1. 재귀 함수 정의
# 사전을 기록할 배열, 현재 문자열, 현재 문자열 숫자
def find(data, p, step):
    # 종료 조건 명시: 최대 5글자까지만 가능 
    if step == 6: return
    # 사전 추가
    if p != '': data.append(p)
    # 문자열을 모음 순서대로 합쳐서 다음 재귀 호출
    for c in ['A', 'E', 'I', 'O', 'U']:
        find(data, ''.join([p, c]), step + 1)
        
def solution(word):
    # 2. 함수를 실행해 사전을 만들기
    res = 0
    data = []
    find(data, '', 0)

    # 3. 만들어진 사전에서 주어진 단어가 어디에 있는지
    # 전체 탐색으로 찾기
    for i in range(len(data)):
        if data[i] == word:
            res = i + 1
            break
    return res

print(solution("AAAE"))
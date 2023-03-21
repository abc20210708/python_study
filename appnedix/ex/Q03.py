'''
두 개의 문자열을 입력받아, 
두 문자열이 애너그램(Anagram) 
여부를 판별하는 함수를 구현하세요. 
(애너그램: 서로 다른 단어나 
문구의 문자를 재배열하여 다른 뜻을 
가진 단어나 문장으로 바꾸는 것)

예시 입력: "listen", "silent"
예시 출력: True

'''

s1 = "listen"
s2 = "silent"

def solution(s1, s2):
    # 두 문자열의 길이가 다르면 애너그램이 아님
    if len(s1) != len(s2):
        return False
    
    # 각 문자의 등장 횟수를 저장할 딕셔너리 생성
    char_cnt = {}
    for char in s1:
        if char in char_cnt:
            char_cnt[char] += 1
        else:
            char_cnt[char] = 1
    
    # 두 번째 문자열의 각 문자를 하나씩 확인하면서
    # 등장횟수를 감소시키고, 딕셔너리 내에 해당문자가
    # 없거나 등장횟수가 0보다 작아지면 애너그램이 아님
    for char in s2:
        if char not in char_cnt or char_cnt[char] == 0:
            return False
        char_cnt[char] -= 1
        
    # 모든 문자에 대해 등장횟수가 정확히 일치하면 애너그램
    return True

print(solution(s1, s2))
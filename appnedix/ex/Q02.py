'''
문자열을 입력받아, 
각 문자가 몇 번 등장하는지 
딕셔너리 형태로 반환하는 함수를 구현하세요.

예시 입력: "hello"
예시 출력: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
'''

s = "hello"

def solution(s):
    char_cnt = {}
    for char in s:
        if char in char_cnt:
            char_cnt[char] += 1
        else:
            char_cnt[char] = 1
    return char_cnt

print(solution(s))
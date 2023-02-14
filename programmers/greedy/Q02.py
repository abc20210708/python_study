# 큰 수 만들기

# 참고 블로그 https://chiefcoder.tistory.com/37

def solution(number, k):
    answer = [] # stack

    for i in number:
        while k > 0 and answer and answer[-1] < i:
            answer.pop()
            k -= 1
        answer.append(i)

    return ''.join(answer[:len(answer) - k])

print(solution("1924", 2))
# 큰 수 만들기

# 참고 블로그 https://chiefcoder.tistory.com/37

def solution(number, k):
    answer = [] # stack

    for i in number:  # 숫자 문자열을 한 자리씩 반복하면서
        while k > 0 and answer and answer[-1] < i:
            # k가 0보다 크고, answer가 비어있지 않고, answer의 마지막 요소가 현재 숫자보다 작을 때
            answer.pop()  # answer에서 마지막 요소를 제거
            k -= 1  # 제거한 횟수를 1 감소시킴
        answer.append(i)  # 현재 숫자를 answer에 추가

    return ''.join(answer[:len(answer) - k])
    # answer에서 k만큼의 숫자를 제외한 나머지 숫자들을 문자열로 변환하여 반환

print(solution("1924", 2))

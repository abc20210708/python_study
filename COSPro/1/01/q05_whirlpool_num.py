## 문제5) 소용돌이 수
#  참고 블로그 https://whatryando.tistory.com/125

def solution(n):
    res = 0
    
    if n == 1:
        return 1
    if n == 2:
        return 4
    else:
        res = n*2 + (n-1)*4*(n-2) + solution(n-2)
    return res


n1 = 3
ret1 = solution(n1)

print("solution 함수의 반환 값은", ret1, "입니다.")
    
n2 = 2
ret2 = solution(n2)

print("solution 함수의 반환 값은", ret2, "입니다.")
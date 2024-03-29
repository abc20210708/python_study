## 문제 6) 369 게임 박수의 갯수 구하기 - Python3
#  참고 블로그 https://popooly.tistory.com/208

def solution(number):
    cnt = 0
    
    for i in range(1, number +1):
        current = i
        tmp = cnt
        while current != 0:
            if str(current)[-1] in ['3', '6', '9']: # or current%10 in [3, 6, 9]
                cnt += 1
                print("pair", end='')
            current = current // 10
        if tmp == cnt:
            print(i, end='')
        print(" ", end='')
    print("")
    return cnt



# AC (골드 5) 다른 풀이
# 참고 블로그 https://it-garden.tistory.com/288


import sys
input = lambda : sys.stdin.readline().strip()

t = int(input())

for i in range(t):
    p = input()
    n = int(input())
    de = input()[1:-1].split(',')
    # R이 연속 2번이면 원래와 같기 때문에
    p = p.replace("RR", '')
    
    r = 0 # R의 개수
    # f는 앞에서부터 버려야 하는 요소의 개수
    # b는 뒤에서부터 버려야 하는 요소의 개수
    f, b = 0, 0
    
    for j in p:
        if j == "R":
            r += 1
        elif j == "D":
            # r이 짝수이면 앞에서부터 빼야하기 때문에
            # f에 1을 더하기
            if r % 2 == 0:
                f += 1
            # r이 홀수면 뒤에서부터 빼야하기 때문에
            # b에 1을 더하기
            else:
                b += 1
    
    if f + b <= n:
        de = de[f:n-b]
        
        if r % 2 == 1:
            print('['+','.join(de[::-1])+']')
        else:
            print('['+','.join(de)+']')
    else:
        print('error')
    
    

    
    
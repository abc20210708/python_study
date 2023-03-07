# 캠핑 다시 풀기

'''
연속하는 20일 중 10일 사용
28일 휴가

연속하는 P일 중, L일 동안 사용 가능
V일짜리 휴가 시작,  최대 며칠동안 사용가능한가?

5 8 20
5 8 17
0 0 0

Case 1: 14
Case 2: 11

'''

i = 0

while True:
    i += 1
    l, p, v = map(int, input().split())
    if l + p + v == 0: break
    num = ((v //p) * l) + min(l, v % p)
    print(f'Case {i}:', num)
    
    
    
    



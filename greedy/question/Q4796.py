
# 캠핑
# 참고 블로그 https://codingpractices.tistory.com/entry/%EA%B7%B8%EB%A6%AC%EB%94%94-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%985-%EB%B0%B1%EC%A4%80-4796%EB%B2%88-%EC%BA%A0%ED%95%91-%ED%8C%8C%EC%9D%B4%EC%8D%AC

'''
'''
#l, p, v = 5, 8, 20


i = 0
while True:
    i += 1
    l, p, v = map(int, input().split())   
    if l+p+v == 0 : break
    print(f'Case {i}:', ((v//p)*l) + min(l, v * p))
    
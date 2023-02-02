
# 전자레인지

'''
참고 블로그 https://ludere.tistory.com/55
'''
t = 100

if t % 10 != 0 : print(-1)
else :
    for i in [300, 60, 10]:
        print(t // i, end=' ') 
        t %= i
    
# end옵션을 사용하면 그 뒤의 출력값과 이어서 출력한다.
                                #(즉, 줄바꿈을 하지 않게 된다.)
'''
else :
    A = B = C = 0
    A = t // 300
    B = (t % 300) // 60
    C = (t % 300) % 60 // 10
    print(A, B, C)
'''
    

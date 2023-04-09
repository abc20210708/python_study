## 공통 순열 (실버 4) *

# 참고 블로그 http://jsggo2001.tistory.com/17

while 1:
    try:
        s1 = input()
        s2 = input()
        res = []
        for i in s1:
            if i in s2:
                res.append(i)
                s2 = s2.replace(i, "", 1)
        res.sort()
        print(''.join(res))
    except:
        break
        
'''
추가하는 과정에서 b.replace(i, "", 1) 코드가 사용되는데, 
이 코드는 문자열 b에서 첫 번째로 등장하는 문자 i를 제거하는 역할을 합니다.

예를 들어, b가 "hello"이고 i가 "l"이라면 
b.replace(i, "", 1)을 실행하면 "helo"가 반환됩니다. 
이를 이용하여 str1에서 str2에 있는 문자열을 제거하는 것으로, 
중복되는 문자열이 출력되는 것을 방지합니다.
'''
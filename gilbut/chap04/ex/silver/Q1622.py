## 공통 순열 (실버 4) *

# 참고 블로그 http://jsggo2001.tistory.com/17

while 1:
    try:
        str1 = input()
        str2 = input()
        
        arr = []
        for i in str1:
            if i in str2:
                arr.append(i)
                b = b.replace(i, "", 1)
        arr.sort()
        print(''.join(arr))
    except:
        break
        
    
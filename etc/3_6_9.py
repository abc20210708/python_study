## 3, 6, 9 구현

'''
구현 기준
정수 n을 입력받는다.

1부터 입력받은 정수 n까지 한칸씩 띄어 
순서대로 출력하되,

3, 6, 9가 포함된 경우 박수(X)를 친다.
3, 6, 9가 여러 개 포함된 숫자의 경우, 
포함된 숫자만큼 박수를 친다.
'''

import re


print("1부터 숫자를 입력하세요 :)")


try:
    n = int(input())
    for i in range(1, n+1):
        tmp = str(i)
        tmp = tmp.replace("3", "_").replace("6", "_").replace("9", "_")
        # 만약 문자열에서 모든 문자열이 숫자면
        if tmp.isdigit():
            print(i, end=" ")
        else:
            tmp = re.sub(r'[0-9]+', '', tmp)
            print("X" * len(tmp), end=" ")     
            
                  
except ValueError:
    print("에러!! 숫자를 입력하세요 :)")
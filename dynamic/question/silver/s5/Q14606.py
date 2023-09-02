## 피자 small (실버 5)
#  참고 블로그 https://jinho-study.tistory.com/971


import sys
input = sys.stdin.readline

n = int(input()) # 피자판의 개수

if n == 1:
    print(0)
    exit()
    
print(n * (n-1) // 2)

'''
chatGPT 검색

요약하면, 두 함수 모두 프로그램을 종료하는 데 사용되며, 
exit(0)은 명시적으로 리턴 코드를 0으로 설정하는 것이고,
exit()은 기본적으로 0을 리턴하는 것입니다. 

일반적으로 프로그램이 정상적으로 종료되었을 때 0을 리턴하고, 
에러가 발생하거나 비정상적으로 종료되었을 때 다른 값을 리턴하는 것이 관례입니다.
'''
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

(n * (n - 1) // 2) 식은 정수 n을 사용해 조합의 개수를 계산할 때 사용하는 수식

이 식은 "n 개에서 2개를 선택하는 조합의 개수"를 나타냅니다.

일반적으로 조합의 개수는 다음과 같이 표현됩니다:

scss
Copy code
C(n, r) = n! / (r! * (n - r)!)
여기서 C(n, r)은 n개 중에서 r개를 선택하는 조합의 개수를 나타내며, 
n!은 n 팩토리얼(n부터 1까지의 모든 양의 정수를 곱한 값)을 의미합니다. 
그러나 r이 2인 경우, 즉 2개를 선택하는 경우를 다루기 위해서 
위 식을 단순화한 것이 (n * (n - 1) // 2)입니다.

따라서 (n * (n - 1) // 2) 식은 정수 n을 사용하여
"n 개 중에서 2개를 선택하는 조합의 개수"를 효율적으로 
계산하는 수식으로 사용됩니다.

'''


'''
## 참고 블로그 https://gyong0117.tistory.com/entry/BOJ%EB%B0%B1%EC%A4%80-14606C-%ED%94%BC%EC%9E%90-Small
일단, 높이가 A인 탑을 분리하여 가장 큰 즐거움을 얻기 위해서는, 
분리하는 두 탑의 높이가 같거나 높이가 1 차이여야 한다.

ex) 7 => (1,6) (2,5) (3,4) => (3,4)로 나눌 때가 가장 값이 커진다.

ex) 6 => (1,5) (2,4) (3,3) => (3,3)으로 나눌 때가 가장 값이 커진다.

 
'''


'''
chatGPT 검색

요약하면, 두 함수 모두 프로그램을 종료하는 데 사용되며, 
exit(0)은 명시적으로 리턴 코드를 0으로 설정하는 것이고,
exit()은 기본적으로 0을 리턴하는 것입니다. 

일반적으로 프로그램이 정상적으로 종료되었을 때 0을 리턴하고, 
에러가 발생하거나 비정상적으로 종료되었을 때 다른 값을 리턴하는 것이 관례입니다.
'''
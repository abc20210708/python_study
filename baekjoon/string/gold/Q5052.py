## 전화번호 목록 (골드 4) *

# 참고 블로그 https://fre2-dom.tistory.com/209
import sys
input = sys.stdin.readline

t = int(input()) # 테스트 케이스의 개수를 입력받음
for _ in range(t):
    n = int(input()) # 전화번호의 수를 입력받음
    # 전화번호를 입력받아 배열에 저장
    arr = [input().strip() for _ in range(n)] 
    arr.sort() # 전화번호를 사전순으로 정렬
    check = "yes" # 일관성 여부를 나타내는 변수, 처음에는 "yes"로 초기화

# 반복문을 통해 전화번호를 확인
for i in range(len(arr) - 1):
    # 만약 현재 전화번호가 다음 전화번호의 접두어인 경우
    if arr[i] == arr[i+1][0:len(arr[i])]:
        check = "no" # 일관성이 없음을 표시
        break # 반복문 종료
        
if check == "no":
    print("NO") # 일관성이 없는 경우 "NO" 출력
else:
    print("YES") # 일관성이 있는 경우 "YES" 출력 
    
'''
"접두어"란, 한 문자열이 다른 문자열의 앞 부분에 포함되는 경우를 말합니다. 
예를 들어, "abc"가 "abcdef"의 접두어인 경우 "abcdef"라는 
문자열의 시작 부분이 "abc"로 시작하므로 "abc"는 "abcdef"의 접두어입니다.

위 코드에서는 현재 전화번호가 다음 전화번호의 접두어인지를 비교하여, 
만약 접두어인 경우에는 일관성이 없다고 판단하고 "NO"를 출력하고 있습니다. 
이는 한 번호가 다른 번호의 접두어로 포함되는 경우, 
예를 들어 "911"이 "91125426"의 접두어인 경우에는 일관성이 없는 목록으로 
처리하기 위한 로직입니다.
'''
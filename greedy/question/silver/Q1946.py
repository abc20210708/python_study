## 신입사원 (실버 1)*

# 참고한 코드 https://www.acmicpc.net/source/24856513
import sys
input = sys.stdin.readline

# 문제 해결을 위한 함수 정의
def solve():
    # 지원자 수 입력
    n = int(input())

    # 지원자의 점수를 저장할 리스트 생성
    scores = [0] * (n + 1)

    # 각 지원자의 서류심사 등수와 면접심사 등수 입력받아서 리스트에 저장
    for _ in range(n):
        paper, interview = map(int, input().split())
        scores[paper] = interview

    # 첫 번째 지원자의 면접심사 등수를 초기 기준값으로 설정
    cutline = scores[1]

    # 선발된 지원자의 수를 저장할 변수 초기화
    count = 1

    # 두 번째 지원자부터 반복하여 비교
    for i in range(2, n+1):
        # 현재 지원자의 면접심사 등수가 기준값보다 낮을 경우
        if scores[i] < cutline:
            # 선발된 지원자의 수를 증가시키고
            count += 1
            # 기준값을 현재 지원자의 면접심사 등수로 갱신
            cutline = scores[i]

    # 선발된 지원자의 수를 문자열로 변환하여 반환
    return str(count)

result = []

# 테스트 케이스 수 입력
for _ in range(int(input())):
    # solve 함수를 호출하여 결과를 리스트에 저장
    result.append(solve())

# 각 테스트 케이스의 결과를 개행 문자를 기준으로 구분하여 출력
print("\n".join(result))

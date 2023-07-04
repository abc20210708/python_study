## 카드 숫자 곱의 경우의 수 (실버 3) *
# 참고 블로그 https://readble-ko.tistory.com/137


N = int(input())

# 각 숫자의 사용 여부를 체크할 리스트를 생성
# 최대 5000000까지의 숫자를 체크할 수 있도록
checker = [False] * 5000000

answer = 0

# 초기 배열을 생성한다. 배열의 첫 번째 요소는 1로 설정
arr = [1]

# 1은 이미 체크되어 있다고 가정하고 체크 리스트에서 체크
checker[1] = True

# N번 반복하여 N자리 수를 만들기 위한 모든 경우의 수를 구한다.
for _ in range(N):
    # 현재 배열의 크기를 저장
    size = len(arr)
    
    # 현재 배열에 대해서 모든 요소에 대해 반복
    for j in range(size):
        # 각 요소에 1부터 9까지의 숫자를 곱해서 새로운 수를 만들고 이를 tmp 변수에 저장
        for k in range(1, 10):
            tmp = arr[j] * k
            
            # 새로운 수가 이전에 만들어진 적이 없다면, 즉, checker[tmp]가 False라면
            if not checker[tmp]:
                # 해당 수를 체크하고 배열에 추가
                checker[tmp] = True
                arr.append(tmp)

# 모든 경우의 수를 만들었으므로, 배열의 길이를 출력, 이는 N자리 수를 만들 수 있는 서로 다른 숫자의 개수를 의미
print(len(arr))
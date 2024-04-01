## 문제4) 합이 k 배가 되는 수

def solution(arr, K):
    res = 0
    
    length = len(arr)
    
    for i in range(length):
        for j in range(i+1, length):
            for k in range(j+1, length):
                if (arr[i]+arr[j]+arr[k]) % K == 0:
                    res += 1
                    
    return res


arr = [1, 2, 3, 4, 5]
K = 3
ret = solution(arr, K)

print("solution 함수의 반환 값은", ret, "입니다.")
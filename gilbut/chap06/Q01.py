## 조합과 순열

'''
 선택되는 원소의 순서가 매우 중요하다면 
 ==>순열
 
 반대로 조합은 순서가 달라도 데이터가 같다면,
 동일한 경우로 취급
 따라서 가능한 가짓수 자체를 뽑아내는 것이 목적이면
 ==>조합
 
 기본적인 순열이나 조합과 동일하지만 같은 원소를
 다시 택하는 것이 가능
 ==> 중복순열/중복조합
 
'''
## 방법 1. 반복문 (주어진 배열에서 가능한 순열을 만듦)
def permutations_1(arr):
    # 처음 인덱스 생성
    # (arr을 그대로 넣으면 얕은 복사가 발생)
    result = [arr[:]] 
    # 배열끼리 위치를 바꾸기 위한 인덱스 배열
    c = [0] * len(arr)
    i = 0
    # 배열 조작을 위한 반복문
    while i < len(arr):
        if c[i] < i:
            if i % 2 == 0:
                arr[0], arr[i] = arr[i], arr[0]
            else:
                arr[c[i]], arr[i] = arr[i],  arr[c[i]]
            result.append(arr[:]) # 새로운 초기 데이터 생성
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    return result

print(permutations_1([1,2,3]))    
        
## 방법2. 재귀(전체에서 n개를 뽑아서 만드는 기능 지원)
def permutations_2(arr, n):
    result = []
    if n == 0 : return [[]]
    
    #([0,1,2,3], 2) = ([0],([1,2,3], 1)) + ([1],([0,2,3], 1)) 
    #                   + ([2], ([0,1,3], 1)) + ([3], ([0,1,2]), 1)
    for (i, num) in enumerate(arr):
        for j in permutations_2(arr[:i] + arr[i + 1:], n - 1):
            result.append([num] + j)
    return result

print(permutations_2([1,2,3], 3))
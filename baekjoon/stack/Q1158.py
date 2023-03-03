# 요세푸스 문제


'''
N명의 사람들이 있고, K를 주기로 사람들을 제거하는 문제
이때 K(주기)가 사람의 인원수를 초과하면

사람의 인원수로 나눈 나머지로 값을 초기화하면 된다.

참고 블로그 https://infinitt.tistory.com/213
'''

n, k = map(int, input().split())
# 맨 처음에 원에 앉아있는 사람들
arr = [i for i in range(1, n+1)]

# 제거된 사람들을 넣을 배열
result = []
# 제거된 사람의 인덱스 번호
num = 0

for _ in range(n):
    num += k-1
    if num >= len(arr):
        num = num % len(arr)
    result.append(str(arr.pop(num)))

#   result.append(str(arr[num]))
#   arr.pop(num)
    

print("<",", ".join(result),">", sep='')

'''
sep(separation) 
 

영단어 그대로, 분리하여 출력한다. 
다만 분리할 (갈라놓을 문자를 지정할 수 있다.) 
이것을 구분자라고 한다.

예를 들어서 아래처럼 사용 할 수 있다.

print('S','E','P', sep='@')

출력 >>>>> S@E@P
'''

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
    
print(f"<{', '.join(map(str,answer))}>")
#print("<",", ".join(result),">", sep='')

'''
def josephus(n, k):
    people = list(range(1, n+1))
    result = []
    idx = 0
    
    while people:
        idx = (idx + k - 1) % len(people)
        result.append(people.pop(idx))
    
    return result[-1]
    
이 함수는 두 개의 인자 n과 k를 받아서 요세푸스 문제를 해결합니다. 
리스트 people에 1부터 n까지의 숫자를 넣고, while 루프를 사용해서 
요세푸스 문제를 해결합니다. while 루프 내에서는 인덱스 idx를 사용해서 
리스트에서 요소를 제거하고, 결과를 result 리스트에 저장합니다. 
마지막으로, 결과 리스트의 마지막 요소를 반환합니다.

예를 들어, josephus(7, 3)을 호출하면 [3, 6, 2, 7, 5, 1]이 반환됩니다. 
마지막으로, 리스트의 마지막 요소인 1이 반환됩니다.
'''



'''
sep(separation) 
 

영단어 그대로, 분리하여 출력한다. 
다만 분리할 (갈라놓을 문자를 지정할 수 있다.) 
이것을 구분자라고 한다.

예를 들어서 아래처럼 사용 할 수 있다.

print('S','E','P', sep='@')

출력 >>>>> S@E@P
'''

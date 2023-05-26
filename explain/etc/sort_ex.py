## 인덱스 원소를 크기 순으로 정렬
'''
리스트 내 원소를 크기순으로 정렬했을 때의
인덱스가 어떻게 정렬되는지가 필요할 때가 있다.
예를 들어 A리스트의 크기 순서대로 똑같이 맞추어
B리스트를 정렬하고자 할 때는, A 리스트의 인덱스의
정렬 정보가 필요한 것이다.
'''
# 참고 블로그 https://daeun-computer-uneasy.tistory.com/74

b = [12, 14, 23, 24, 16]
b_idx = sorted(range(len(b)), key=lambda k:b[k])

print(b_idx) # [0, 1, 4, 2, 3]

'''
sorted 함수에서 key 매개변수에 전달된 람다 함수는 각 요소의 
인덱스를 입력으로 받아 해당 인덱스에 해당하는 요소의 값으로 정렬을 수행합니다.

따라서 b_idx는 정렬된 결과로, 가장 작은 값인 12의 인덱스는 0, 
다음으로 작은 값인 14의 인덱스는 1, 그 다음으로 작은 값인 16의 인덱스는 4, 
23의 인덱스는 2, 24의 인덱스는 3이 됩니다.

따라서 b_idx는 [0, 1, 4, 2, 3]이 되는 것입니다.

'''

b_idx = sorted(b_idx, key=lambda k: b_idx[k])
print(b_idx) # [0, 1, 3, 4, 2]
## b_idx를 sorted 함수에 전달하는 대신 인덱스를 
# 직접 정렬한 후에 그 결과를 사용해야 합니다. 
# 다음과 같이 코드를 작성할 수 있습니다:


'''
"두 개의 리스트에서 모든 조합을 계산할 때는 product 메서드를 사용한다"는 
문장은 일반적으로 파이썬의 itertools 모듈에서 제공되는 product 함수를 의미하는 것 같습니다.

itertools 모듈은 파이썬의 내장 라이브러리로, 이터레이터를 다루는 데 유용한 함수들을 제공합니다. 
product 함수는 itertools 모듈 안에 있는 함수 중 하나로, 여러 개의 리스트에서 가능한 모든 조합을 
계산해주는 기능을 제공합니다.

예를 들어, product 함수를 사용하여 [1, 2]와 [3, 4]라는 두 개의 리스트로부터 가능한 모든 조합을 
계산하고 싶다면, 다음과 같이 코드를 작성할 수 있습니다:
'''

from itertools import product

a = [1, 2]
b = [3, 4]

combinations = list(product(a, b))
print(combinations)  # [(1, 3), (1, 4), (2, 3), (2, 4)]
'''
위 코드를 실행하면, 출력 결과로 [(1, 3), (1, 4), (2, 3), (2, 4)]라는 리스트가 나옵니다. 
각 튜플은 첫 번째 리스트의 요소와 두 번째 리스트의 요소를 조합한 결과를 나타냅니다.

즉, product 함수는 두 개 이상의 리스트에서 가능한 모든 조합을 계산해주는 기능을 제공합니다.

'''


'''
## A.sort( )  / sorted( 리스트 )
sorted( 리스트 )는 새로 정렬된 목록을 return 하되, 원래 정렬은 유지된다. 
하지만 sort()는 원래 정렬까지 바꾸고, None을 반환한다. 

+) 참고로 알파벳 순서로도 정렬할 수 있다 !
'''
sorted( [5, 2, 3, 1, 4] )
#[1, 2, 3, 4, 5] # 원본은 그대로 유지됨 

a = [5, 2, 3, 1, 4]
a.sort() 
print(f"a: {a}")
# None # 근데 a는 바뀐상태
# 디폴트는 오름차순이고, 내림차순으로 정렬하고 싶다면 
# sort(reverse=True) 옵션을 사용할 수 있다. 

'''
파이썬의 sorted 함수는 기본적으로 오름차순으로 정렬을 수행합니다. 
그러나 sorted 함수를 사용하여 내림차순으로 정렬하려면 reverse 매개변수를 활용해야 합니다.

sorted 함수의 reverse 매개변수를 True로 설정하면 내림차순으로 정렬됩니다. 
기본값은 False이며, 이는 오름차순 정렬을 의미합니다.

예를 들어, 리스트 a를 내림차순으로 정렬하고 싶다면 다음과 같이 코드를 작성할 수 있습니다:
'''

a = [5, 2, 8, 1, 9]
sorted_a = sorted(a, reverse=True)
print(sorted_a) # [9, 8, 5, 2, 1]
'''
위 코드를 실행하면, 출력 결과로 [9, 8, 5, 2, 1]이 나옵니다. 
리스트 a가 내림차순으로 정렬된 결과입니다.

따라서 sorted 함수를 사용하여 내림차순으로 정렬하고자 할 때는 
sorted(a, reverse=True)와 같이 reverse 매개변수를 활용하면 됩니다.
'''
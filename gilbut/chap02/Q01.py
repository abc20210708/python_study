## 슬라이싱 

print("Python is awesome"[3::2])
# h, n, i, " ", w, s, m

data = [[(0,1), (2,3), (4,5)], [(6,7), (8,9), (0,1)]]
print(data[1:])
print(data[1:][0])
print(data[1:][0][::2])

## 리스트 컴프리 헨션 vs 제너레이터
#  편의성과 효율의 대결

d = []
for i in range(1, 11):
    d.append(i)
    
'''
 한 줄로 줄여 컴프리헨션(comprehension)을 사용
 [i for ii n range(1,11)]
 [(변수 표현식) for (사용할 변수) in (순화 가능한 연속적인 데이터)]
 선언 -> 할당 -> 재구성 과장을 단 할 줄에 끝낼 수 있다
'''

# [i for i in range(11) if i % 2 == 0 if i % 5 == 0]
'''
if문 뒤에 if문을 중첩할 수 있지만, 이때 if 문은 and로 취급
직접적으로 and를 넣으면 오류가 발생
마찬가지로 or도 사용할 수 없습니다.
'''


## 리스트 컴프레헨션
comprehension = [num ** 2 for num in range(1000000)]
## 제너레이터
generator = (num ** 2 for num in range(1000000))
'''
제너레이터는 연속 가능한 자료형을 반환하는 함수로,
실행 중 yield를 만나면 값을 반환하고 더 이상 진행할 수 없는
상태가 아니라면 next()가 호출되기 전까지 대기

한 번에 모두 실행하고 그에 대한 결괏값을 반환하는 것이 아니라,
함수가 실행되었다가 다음 next()를 대가하면서 실행이 멈춤

제네러이터를 만드는 방법은 
1. 함수를 정의할 떄 return 대신 yield 문구
2. 컴프리헨션 문구를 소괄호로 감싸는 방식

참고 블로그 https://velog.io/@jewon119/TIL30.-Python-%EC%A0%9C%EB%84%88%EB%A0%88%EC%9D%B4%ED%84%B0Generator-%EA%B0%9C%EB%85%90-%EC%A0%95%EB%A6%AC
'''



## 값 범위 할당
sample = [0, 1, 2, 3, 4, 5]
print(sample)
sample[1:4] = [9,9,9]
print(sample)

set1 = {1, 2, 3, 'a', 'b', 'c'}
set1.remove(1)

#set1.remove(1)
'''
에러 발생 이유는 집합에서 1이라는 값을
제거하라고 했지만 이미 1이라는 값을 제거해서 없다.
그래서 KeyError가 발생
'''

set1.discard(1)

'''
지우라는 키가 집합에 없어도 에러가 발생하지 않는다
remove()s는 실제 존재하는 엘리먼트를 지우는 동작에 사용
discard()는 집합에 존재하지 않음을 보장하려고 할 때 사용

참고 블로그 https://hbase.tistory.com/111
'''
print(set1)


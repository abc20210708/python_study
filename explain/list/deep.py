## 얕은 복사, 깊은 복사
#  참고 블로그 https://jie0025.tistory.com/208

# list, set, dict, class : mutable (가변) 객체
# bool, int, float, tuple, str: immutable(불가변) 객체

'''
 얕은 복사

같은 메모리 주소를 가리키는 복사
이 경우 결과적으론 같은 것을 가리키기 때문에,
메모리에 들어있는 값이 바뀌면 동시에 값이 바뀐다.
'''
a = [1, 2]
b = a
b[1] = 1000
print(a) # [1000, 2]

# 따라서 새로운 객체를 만들고 싶다면 import copy를 해준 다음,
# copy.deepcopy(복사할 대상)을 사용해야 한다.

### 궁금해서 [:]로 적용
d = a[:]
d[1] = 88
print(f"a : {a}") # [1, 1000]
print(f"d : {d}") # [1, 88]
# a가 같이 변하지 않음!


'''
 깊은 복사
 
아에 새롭게 만드는 복사 (내부 객체까지)

immutable 불가변 객체는 마찬가지로 대입 연사자를 사용할 경우
같은 메모리 주소를 갖긴 하지만, b에 다른 값을 대입할 때,
재할당을 통해 메모리 주소가 변경된다.

'''
import copy
c = copy.deepcopy(a)
c[1] = 999
print(a) # [1000, 2]
print(c) # [999, 2]
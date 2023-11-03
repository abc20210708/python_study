## enumerate
#  참고 블로그 https://velog.io/@turningtwenty/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%82%B4%EC%9E%A5%ED%95%A8%EC%88%98-enumerate

'''
순서가 있는 자료형(list, set, tuple, dictionary, string)을 입력으로 받았을 때, 인덱스와 값을 포함하여 리턴
for문과 함께 자주 사용됨
인덱스와 값을 동시에 접근하면서 루프를 돌리고 싶을 때 사용 
'''
# enumerate(순서가 있는 객체, start=0)
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
# 이 fruits 리스트를 예시로 들어보자.

print(fruits) 
#['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

print(list(enumerate(fruits))) 
#[(0, 'orange'), (1, 'apple'), (2, 'pear'), (3, 'banana'), (4, 'kiwi'), (5, 'apple'), (6, 'banana')]

# 문자열과 딕셔너리에도 사용할 수 있다.

str = "banana"
for _ in enumerate(str):
  print(_, end = " ") #(0, 'b') (1, 'a') (2, 'n') (3, 'a') (4, 'n') (5, 'a') 
 
print()  
  
dic = {"a":1, "b":2, "c":3, "d":4, "e":5}
for d in enumerate(dic):
  print(d, end = " ") #(0, 'a') (1, 'b') (2, 'c') (3, 'd') (4, 'e') 
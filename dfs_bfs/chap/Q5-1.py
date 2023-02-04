# 스택 예제

stack = []

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7)
# 삭제() - 삽입(1) - 삽입(4) - 삭제()

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) # 최하단 원소부터 출력
print(stack[::-1]) # 최상단 원소부터 출력

'''
파이썬에서 스택을 이용할 때에는 별도의 라이브러리를 사용할 필요가 없다.
append(), pop() 메서드를 이용하면 스택 자료구조와 동일하게 동작한다
append() - 리스트의 가장 뒤족에 데이터를 삽입
pop() - 리스트의 가장 뒤족에서 데이터를 꺼냄
'''
## 딕셔너리

d = {'a': 1, 'b': 2, 'c': 3}

print(d.get('d')) # None

'''
get()메서드 두 개의 인자 일 때,
첫 번째 인자는 찾고자하는 key 값,
두 번째 인자는 key가 없을 대 리턴할 값을 default로
'''

print(d.get('d', 9)) 

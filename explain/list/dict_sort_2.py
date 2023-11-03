## Sorted 정렬 (Key 2개)

a = [(1, -1), (1, 2), (2, 2), (3, 3), (0, 4)]

print(sorted(a , key = lambda x : (x[1] , -x[0]) ))
# [(1, -1), (2, 2), (1, 2), (3, 3), (0, 4)]
# y축으로 정렬 x축으로 내림차순 정렬


## 딕셔너리 정렬
#  참고 블로그  https://velog.io/@winckey0/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%BD%94%ED%85%8C-%ED%95%A8%EC%88%98-%EA%B3%84%EC%82%B0

d = {'blockdmask': 400, 'equal': 300, 'apple': 200, 'dish': 100, 'cook': 500}
 
print('1. 원본 딕셔너리')
print(d.items())
# dict_items([('blockdmask', 400), ('equal', 300), ('apple', 200), ('dish', 100), ('cook', 500)])


print('\n2. 딕셔너리 정렬 : sorted(d.items())')
f = sorted(d.items())
print(f) 
# [('apple', 200), ('blockdmask', 400), ('cook', 500), ('dish', 100), ('equal', 300)]

print('\n3. 딕셔너리 정렬 : sorted(d.items(), key=lambda x: x[1])')
g = sorted(d.items(), key=lambda x: x[1]) # value 기준정렬 key=lambda x: x[1]
print(g) # 단 튜플형태로 변경
 
dicts = dict(sorted(d.items(), key=lambda x: x[1]))
print(g) # 딕션너리로 반환


print('\n4. 딕셔너리 정렬 : sorted(d.items(), key=lambda x: x[1], reverse=True)')
h = sorted(d.items(), key=lambda x: x[1], reverse=True)
print(h)






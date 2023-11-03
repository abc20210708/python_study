## 딕셔너리 정렬
#  참고 블로그 https://yang-wistory1009.tistory.com/38

fruits = { 'apple': 2, 'banana' : 1, 'pear' : 2, 'melon' : 0, 'plum' : 1}
print(sum(fruits.values())) #6
# key 기준 정렬
res = sorted(fruits)
print(res) # ['apple', 'banana', 'melon', 'pear', 'plum']

# value 기준 정렬
tmp = sorted(fruits, key=lambda x: fruits[x])
print(tmp) # ['melon', 'banana', 'plum', 'apple', 'pear']


# key 값 기준 오름차순 
price = {"juice":3000, "water":2000, "milk":1500, "apple":7000}
pr = dict(sorted(price.items()))
print(pr) # {'apple': 7000, 'juice': 3000, 'milk': 1500, 'water': 2000}

# 최대, 최소 
print(max(price.values()))
print(min(price.values()))

# 최댓값을 가지는 key, 최솟값을 가지는 key
print(max(price, key=price.get))
print(min(price, key=price.get))


# key 값 기준 내림차순
pr2 = dict(sorted(price.items(), reverse=True))
print(pr2) # {'water': 2000, 'milk': 1500, 'juice': 3000, 'apple': 7000}

# value 기준 오름차순
my_dict = {'c': 3, 'a': 1, 'b': 2, 'e': 1, 'd': 2}
lst1 = dict(sorted(my_dict.items(), key=lambda x:x[1]))
print(lst1) # {'a': 1, 'e': 1, 'b': 2, 'd': 2, 'c': 3}

# value 기준 내림차순
lst2 = dict(sorted(my_dict.items(), key=lambda x:-x[1]))
# lst2 = sorted(my_dict, key=lambda x:-my_dict[x])
# #['c', 'b', 'd', 'a', 'e']
print(lst2) # {'c': 3, 'b': 2, 'd': 2, 'a': 1, 'e': 1}


## get() 함수 사용
# get함수는 선언된 dict에서 출력하고자 하는 key가 있으면, 
# 그에 해당하는 value를 출력해줍니다.
# 또한, 출력하고자 하는 key가 없으면, 오류가 아닌 None을 출력합니다.
# print(price.get('banana', '없음'))
price.setdefault('banana', 2300)
print(price)




fruits = { 'apple': 2, 'banana' : 1, 'pear' : 2, 'melon' : 0, 'plum' : 1}

# key 기준 정렬
r = sorted(fruits)
print(r) # ['apple', 'banana', 'melon', 'pear', 'plum']

# value 기준 정렬
r2 = sorted(fruits, key=lambda x:fruits[x])
print(r2) # ['melon', 'banana', 'plum', 'apple', 'pear']

# r2 = sorted(fruits, key=lambda x:x[1])
#['banana', 'pear', 'melon', 'plum', 'apple']


'''

r2 = sorted(fruits, key=lambda x:fruits[x])
print(r2) # ['melon', 'banana', 'plum', 'apple', 'pear']
이 코드는 fruits 딕셔너리를 정렬합니다. 
정렬의 기준은 key 매개변수에 전달된 람다 함수에 따라 결정됩니다. 
여기서 람다 함수는 각 항목을 받아 해당 항목의 값을 
fruits 딕셔너리에서 찾아서 그 값을 기준으로 정렬합니다. 
딕셔너리 값에 따라 정렬되며, 
결과는 ['melon', 'banana', 'plum', 'apple', 'pear']와 
같이 딕셔너리 값의 오름차순으로 정렬됩니다.

두 번째 코드:
r2 = sorted(fruits, key=lambda x:x[1])
# ['banana', 'pear', 'melon', 'plum', 'apple']
이 코드는 fruits 딕셔너리를 정렬합니다. 
이번에는 람다 함수가 각 항목을 받아 해당 항목의 
두 번째 문자 (인덱스 1)를 기준으로 정렬합니다. 
따라서 결과는 ['banana', 'pear', 'melon', 'plum', 'apple']와 
같이 각 항목의 두 번째 문자에 따라 오름차순으로 정렬됩니다.

요약하면, 첫 번째 코드는 딕셔너리 값에 따라 정렬하고, 
두 번째 코드는 각 항목의 두 번째 문자에 따라 정렬합니다.
'''
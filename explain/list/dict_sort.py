## 딕셔너리 정렬

fruits = { 'apple': 2, 'banana' : 1, 'pear' : 2, 'melon' : 0, 'plum' : 1}

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

# key 값 기준 내림차순
pr2 = dict(sorted(price.items(), reverse=True))
print(pr2) # {'water': 2000, 'milk': 1500, 'juice': 3000, 'apple': 7000}

# value 기준 오름차순
my_dict = {'c': 3, 'a': 1, 'b': 2, 'e': 1, 'd': 2}
lst1 = dict(sorted(my_dict.items(), key=lambda x:x[1]))
print(lst1) # {'a': 1, 'e': 1, 'b': 2, 'd': 2, 'c': 3}

# value 기준 내림차순
lst2 = dict(sorted(my_dict.items(), key=lambda x:-x[1]))
print(lst2) # {'c': 3, 'b': 2, 'd': 2, 'a': 1, 'e': 1}
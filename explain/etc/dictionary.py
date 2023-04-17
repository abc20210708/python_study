
book = { 'Apple': 4, 'Banana':11, 'Cherry':7 }

for fruit in book:
    print(fruit) # Key 출력
    
for fruit in book:
    print(book[fruit]) # 값 출력
    
print(book.get('Banana'))
# 딕셔너리의 키에 속하지 않는다면 None 출력
print(book.get('Watermelon')) 
# 0을 출력
print(book.get('Blueberry', "0"))
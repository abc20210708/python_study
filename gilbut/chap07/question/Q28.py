## 가장 큰 수

def explain(numbers):
    numbers = [str(x) for x in numbers]
    numbers.sort(key=lambda x: x*3, reverse=True)
    res = ''.join(numbers)
    if '0' * len(numbers) == res: return '0'
    return res
    
print(explain([6, 10, 2]))

from functools import cmp_to_key

def new_solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=cmp_to_key(lambda x, y: int(x + y)- int(y+x)), reverse=True)
    return str(int(''.join(numbers)))

print(new_solution([6, 10, 2]))
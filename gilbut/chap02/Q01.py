## 슬라이싱 

print("Python is awesome"[3::2])
# h, n, i, " ", w, s, m

data = [[(0,1), (2,3), (4,5)], [(6,7), (8,9), (0,1)]]
print(data[1:][0][::2])

## 리스트 컴프리 헨션 vs 제너레이터
#  편의성과 효율의 대결

d = []
for i in range(1, 11):
    d.append(i)
    
# 한 줄로 줄여 컴프리헨션(comprehension)을 사용
# [i for ii n range(1,11)]
# [(변수 표현식) for (사용할 변수) in (순화 가능한 연속적인 데이터)]

# [i for i in range(11) if i % 2 == 0 if i % 5 == 0]


## 리스트 컴프레헨션
comprehension = [num ** 2 for num in range(1000000)]
## 제너레이터
generator = (num ** 2 for num in range(1000000))

## 값 범위 할당
sample = [0, 1, 2, 3, 4, 5]
print(sample)
sample[1:4] = [9,9,9]
print(sample)
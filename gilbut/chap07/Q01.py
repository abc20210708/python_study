## 정렬의 기준 잡기

'''
key : 정렬 기준을 정하는 함수를 기반으로 정렬

reverse: Bool 값을 받아 최종 결과에서 
        오름차순/내림차순의 여부 결정
'''

sample = [[0, 4], [0, 2], [1, 3], [2, 1]]

def second(x):
    return x[1]

print(sorted(sample, key=second))
print(sorted(sample, key=lambda x: x[1]))

'''
정렬 함수 규칙
'''

students = [
    ('kim', 'B+', 18),
    ('lee', 'A+', 21),
    ('jeong', 'A', 18),
]

## 참고 블로그 https://pearlluck.tistory.com/462
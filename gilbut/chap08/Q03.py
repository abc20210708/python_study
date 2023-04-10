
# 4점 간격으로 A부터 Y등급

from bisect import bisect_left
score = [i for i in range(0, 101, 4)]
grade = ''.join([chr(i) for i in range(65, 90)])
students = [84, 92, 56, 38, 61, 77]

for student in students:
    print(grade[25 - bisect_left(score, student)])

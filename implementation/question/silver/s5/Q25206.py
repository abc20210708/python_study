## 너의 평점은 (실버 5)
#  참고 블로그 https://calkolab.tistory.com/entry/baekjoon-python-25206

total = 0.0
res = 0.0

rating = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
grade = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]

for _ in range(20):
    name, num, alpha = input().split()
    num = float(num)
    if alpha != 'P':
        total += num
        res += num * grade[rating.index(alpha)]  

print(f"{res/total:.6f}")

# 딕셔너리 활용
'''
dic = {"A+":4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0,
      'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0 }

 res += num * dic[alpha]
      
'''
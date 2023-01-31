
# 6026 : [기초-값변환] 실수 2개 입력받아 합 계산

'''
실수 2개를 입력받아
합을 출력하는 프로그램을 작성해보자.
'''

n1, n2 = input().split()
c = float(n1) + float(n2)
print(round(c, 2))
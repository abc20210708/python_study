
# 6022 : [기초-입출력] 연월일 입력받아 나누어 출력

'''
입력
6자리 숫자로 이루어진 연월일(YYMMDD)이 입력된다.

출력
년도(YY) 월(MM) 일(DD)을 공백으로 구분해 한 줄로 출력한다.

입력 예시   
200304

출력 예시
20 03 04
'''

s = input()
print(s[0:2], s[2:4], s[4:6])
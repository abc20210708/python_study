## 셀프 넘버 (실버 5)
#  참고 블로그 https://parkgihyeon.github.io/boj/boj4673/

def self_number(num):
    self_num = num
    while num != 0:
        self_num += num % 10 # 오른쪽 끝 숫자 더함
        num //= 10 # 오른쪽 끝 숫자 삭제
    return self_num

res = []
for i in list(range(1, 10001)):
    res.append(self_number(i))
    if i not in res: # 셀프 넘버로 넘어온 값이 1~i 숫자 중에 없는지 확인
        print(i)

        
# for i in list(range(1, 10001)):
# for i in range(1, 10001): 두 코드 모두 정답인 것에 의문을 가짐

'''
# 의문 해결 참고 블로그 https://dojang.io/mod/page/view.php?id=2200

리스트 = list(range(시작, 끝))
>>> b = list(range(5, 12))
>>> b
[5, 6, 7, 8, 9, 10, 11]

'''


'''
내가 작성한 풀이
nums = [1, 3, 5, 7, 9]

for num in nums:
    print(num)

n = 9
while n <= 10000:
    n += 11
    print(n) 
'''
## input()과 sys.stdin
#  참고 블로그 https://developeryuseon.tistory.com/90


import sys
 
#sys.stdin - 여러줄 입력 받을 때
nums = []
for line in sys.stdin:
    nums.append(line)
 
print(nums)
"""
1
2
3
4
5
^Z
['1\n', '2\n', '3\n', '4\n', '5\n']
"""
#sys.stdin은 ^Z를 입력받으면 종료!!
# 위 결과에서 보다시피 개행문자까지 입력되는걸 볼 수 있다.
#따라서 strip()이나 rstrip()으로 제거해 주어야 한다.

nums.append(line.strip())
"""
1
2
3
4
5
^Z
['1', '2', '3', '4', '5']
"""

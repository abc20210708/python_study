# 피카츄 다시 풀기

# pikaqiu

import sys
import re

input = sys.stdin.readline().rstrip()

tmp = re.sub('pi|ka|chu', "", input)

print(tmp)
if not tmp:
    print("YES")
else:
    print("NO")
## 피카츄 (브론즈 1) *

import re

res = re.fullmatch('(pi|ka|chu)+', input())
print("YES" if res != None else "NO")
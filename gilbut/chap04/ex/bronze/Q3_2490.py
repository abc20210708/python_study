## 윷놀이 (브론즈 3)

forms = {3:'A', 2:'B', 1:'C', 0:'D', 4:'E'}

for _ in range(3):
    arr = list(map(str, input().split()))
    print(forms[arr.count("1")])
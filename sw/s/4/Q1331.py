## 나이트 투어 (실버 4)
#  참고 블로그 https://blex.me/@laetipark/%EB%B0%B1%EC%A4%80bojpython-1331%EB%B2%88-%EB%82%98%EC%9D%B4%ED%8A%B8-%ED%88%AC%EC%96%B4

lst = []
chk = True

for _ in range(36):
    lst.append(input())
    
if len(set(lst)) != 36:
    print("Invalid")
    exit()
    
# lst[-1] : 리스트 뒤에서 첫 번째 요소
for i in range(36):
    dRow = abs(ord(lst[i][0])-ord(lst[i-1][0]))
    dCol = abs(int(lst[i][1])-int(lst[i-1][1]))
    if (dRow == 1 and dCol == 2) or (dRow == 2 and dCol == 1):
        continue
    else:
        print("Invalid")
        exit()

if chk:
    print("Valid")
else:
    print("Invalid")
    
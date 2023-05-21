## 수 정렬하기 2 (실버 5)


l = []

for _ in range(int(input())):
    x = int(input())
    l.append(x)
    
l.sort()

for i in l:
    print(i)
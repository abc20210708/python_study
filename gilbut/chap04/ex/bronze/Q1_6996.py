## 애너그램 (브론즈 1) 

n = int(input())
for _ in range(n):
    s1, s2 = map(str, input().split())
    t1 = list(s1)
    t2 = list(s2)
    t1.sort()
    t2.sort()

    if t1 == t2:
        print(f"{s1} & {s2} are anagrams.")
    else:
        print(f"{s1} & {s2} are NOT anagrams.")
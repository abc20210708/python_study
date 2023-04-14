# 애너그램 다시 풀기

for _ in range(int(input())):
    s1, s2 = map(str, input().split())
    a1 = list(s1)
    a2 = list(s2)
    a1.sort()
    a2.sort()
    
    if a1 == a2:
        print(f"{s1} & {s2} are anagrams.")
    else:
        print(f"{s1} & {s2} are NOT anagrams.")
    
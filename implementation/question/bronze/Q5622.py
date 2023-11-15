## 다이얼 (브론즈 2)

dial = [[0], [0],
        ["A", "B", "C"],
        ["D", "E", "F"],
        ["G", "H", "I"],
        ["J", "K", "L"],
        ["M", "N", "O"],
        ["P", "Q", "R", "S"],
        ["T", "U", "V"],
        ["W", "X", "Y", "Z"]]

word = input()
cnt = len(word)

for w in word:
    for i in range(2, len(dial)):
        if w in dial[i]:
            cnt += i
            
print(cnt)
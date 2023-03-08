# 단어 공부 다시 풀기

word = "baaa".upper()
cnt = 0

for i in set(word):
    if word.count(i) > cnt:
        temp = i
        cnt = word.count(i)
    elif word.count(i) == cnt:
        temp = "?"
        
print(temp)

    
    



    
    
    



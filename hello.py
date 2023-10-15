## 마니또 다시 풀기

caseNum = 0

while 1:
    n = int(input())
    if n == 0: 
        break
    manito = dict()
    caseNum += 1
    
    for _ in range(n):
        toYou, toMe = map(str, input().split())
        manito[toYou] = toMe
    
    cnt = 0
    
    while manito:
        tmp = next(iter(manito))
        start = tmp
        end = manito.get(start)
        manito.pop(start)
        
        while end in manito.keys():
            start = end
            end = manito.get(start)
            if end == tmp:
                cnt += 1
            manito.pop(start)
    print(caseNum, cnt)        
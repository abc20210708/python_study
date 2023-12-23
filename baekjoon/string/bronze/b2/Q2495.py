## 연속구간 (브론즈 2)
#  참고 블로그 https://sunchol21.tistory.com/687
for _ in range(3):
    s = str(input())
    mymax = 1
    cnt = 1
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            cnt+=1
        else:
            mymax=max(cnt,mymax)
            cnt=1
    mymax = max(cnt, mymax)
    print(mymax)
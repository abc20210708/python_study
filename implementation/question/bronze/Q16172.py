## 나는 친구가 적다 (브론즈 2)
#  참고 블로그 https://m.blog.naver.com/rkdfoals/222109430858
import re

if __name__ == "__main__":
    s = input()
    k = input()
    t = re.sub('[0-9]','',s)
    if k in t :
        print('1')
    else :
        print('0')
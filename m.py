# Python 문제풀이_가장 많이 등장하는 알파벳찾기
# 참고 블로그 https://velog.io/@hyejiseo-dev/Python-%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%EA%B0%80%EC%9E%A5-%EB%A7%8E%EC%9D%B4-%EB%93%B1%EC%9E%A5%ED%95%98%EB%8A%94-%EC%95%8C%ED%8C%8C%EB%B2%B3%EC%B0%BE%EA%B8%B0

from collections import Counter

string = 'dfdefdgf'

#print(max(set(inp),key=inp.count))

tmp = Counter(string)

values = [i for i in tmp.values()]
values.sort(reverse=True) # 큰 수부터 배열
big = values[0]

res = [i for i, k in tmp.items() if big == k]
res = ''.join(sorted(res)) # 사전순 정렬

print(res)
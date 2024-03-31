## 문제2) 종이 나누어 주기 

def solution(papers, K):
    length = len(papers)
    
    for i, paper in enumerate(papers):
        K -= paper
        if K < 0:
            length = i -1
    return length
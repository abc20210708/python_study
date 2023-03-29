## H-index *

# 오름차순 정렬
def explain(citations):
    citations.sort()
    for idx, citation in enumerate(citations):
        if citation >= len(citations) - idx:
            return len(citations) - idx
    return 0

#  내림차순 정렬
def new_solution(citations):
    citations.sort(reversed=True)
    for idx, citation in enumerate(citations):
        if idx >= citation:
            return idx
        
    return len(citations)
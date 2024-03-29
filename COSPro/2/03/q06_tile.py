## 문제6) 타일 색칠 방법 구하기 - Python3
#  참고 블로그 https://popooly.tistory.com/233

def solution(tile_len):
    res = ''
    com = 'RRRGGB'
    
    # tile_len을 6으로 나눈 나머지가 3이면 RRR 타일로 마무리
    # tile_len을 6으로 나눈 나머지가 5이면 RRRGG 타일로 마무리
    # tile_len을 6으로 나눈 나머지가 0이면 RRRGGB 타일로 마무리
    
    if tile_len % 6 == 1 or tile_len % 6 == 2 or tile_len % 6 == 4:
        res = '-1'
    else:
        for i in range(tile_len):
            res += com[i % 6]
    
    return res

print(solution(11))

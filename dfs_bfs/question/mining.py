## 광물캐기
# 참고 블로그 https://velog.io/@mimmimmu/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EA%B4%91%EB%AC%BC%EC%BA%90%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC
import sys

def solution(picks, minerals):
    # 최대 int 범위 가져오기, 922경이라는 숫자
    res = sys.maxsize  

    # 각 광물 종류(다이아몬드, 철, 돌)의 선택된 개수를 저장하는 리스트
    visited = [0 for _ in range(3)]  
    # 각 광물을 캐는 순서를 저장하는 리스트입니다.
    orders = []  

    def dfs(depth, tired):
        nonlocal res
        # 선택된 개수의 합이 원하는 개수와 같으면 
        # 모든 광물을 선택한 것이므로 탐색을 종료
        if depth == sum(picks):  
            res = min(res, tired)  
            return

        for i in range(3):
            # 선택된 개수가 원하는 개수보다 작은 경우에만 해당 광물을 선택
            if visited[i] < picks[i]:  
                visited[i] += 1  # 해당 광물 선택 개수를 증가
                orders.append(i)  # 해당 광물을 순서에 추가
                plus = calc(depth)  # 선택한 광물로 인해 증가되는 피로도를 계산
                tired += plus  # 총 피로도에 더해줍니다.

                 # 현재 피로도가 최솟값보다 작은 경우에만 다음 탐색을 진행
                if res > tired: 
                    dfs(depth+1, tired)
                # 탐색이 끝났으므로 해당 광물 선택 개수를 다시 감소
                visited[i] -= 1  
                orders.pop()  # 마지막으로 추가한 광물을 순서에서 제거
                # 탐색이 끝났으므로 해당 광물로 인해 증가된 피로도를 감소
                tired -= plus  

    tired_lst = [
        (1,1,1),  # 다이아몬드 선택 시 피로도 증가량
        (5,1,1),  # 철 선택 시 피로도 증가량
        (25,5,1)  # 돌 선택 시 피로도 증가량
    ]

    DIA = 0  # 다이아몬드를 나타내는 상수
    IRON = 1  # 철을 나타내는 상수
    STONE = 2  # 돌을 나타내는 상수

    def calc(depth):
        plus = 0
         # 현재 탐색하는 광물 선택으로 인해 얻을 수 있는 피로도를 계산
        for i in range(depth*5, (depth+1)*5): 
             # 광물 리스트의 범위를 벗어나면 탐색을 종료
            if i >= len(minerals): 
                break
             #해당 광물 선택에 따른 피로도를 더하기
            if minerals[i] == "diamond":  
                plus += tired_lst[orders[depth]][DIA]
            elif minerals[i] == "iron":  
                plus += tired_lst[orders[depth]][IRON]
            elif minerals[i] == "stone": 
                plus += tired_lst[orders[depth]][STONE]

        return plus

    dfs(0, 0)  # DFS 탐색을 시작
    return res  # 최솟값을 반환

    
print(solution([1, 3, 2],
         ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]))





# global nonlocal 차이

# nonlocal 키워드
# 말그대로 해당 변수는 'local이 아니다'고 선언해주는 키워드다. 
# 즉, 상위 함수에 변수를 참조한다고 미리 선언한다는 것이다. 


def test():
   a = 3

   def sum():
       nonlocal a
       a = 7
       return True

   sum()
   return a

result = test()
print(result)
 

#위와 같이 실행하면 7 이라는 값을 의도대로 출력한다.
# nonlocal로 선언함으로써 a 값을 상위 함수의 a 값을 사용한다. 



## 참고 블로그 https://devpouch.tistory.com/194

c = 11
def test():
   a = 3
   b = 9

   def sum():
       nonlocal a
       global b
       a = 7        # nonlocal 변수는 상위 변수의 접근 O
       b = 11       # global 변수는 중첩함수내에서 상위 함수의 변수는 접근 X

       global c
       c = 13       # global 변수는 함수 외부의 변수는 접근 가능
       return True

   sum()
   return a, b, c

result = test()
print(result)     # (7, 9 , 13) 출력


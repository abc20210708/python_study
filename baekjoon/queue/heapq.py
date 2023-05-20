# 최대 힙 

# 참고 블로그 https://velog.io/@yyj8771/Python-heapq%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-%EC%B5%9C%EC%86%8C-%ED%9E%99-%EC%B5%9C%EB%8C%80-%ED%9E%99
# heapq에서는 최대 힙을 제공하지 않는다. 
# 따라서 다음과 같이 부호를 변경하는 방법을 
# 사용해서 최대 힙을 구현한다. 
# 부호를 바꿔서 최소 힙에 넣어준 뒤에 
# 최솟값부터 pop을 해줄 때 다시 부호를 바꿔주면 최대 힙과 동일하다.

import heapq

heap = []
values = [1,5,3,2,4]

# 아래 for문을 실행시키고 나면 heap은 [-5,-4,-3,-1,-2]가 된다.
for value in values:
	heapq.heappush(heap, -value)

# 아래 for문을 실행시키면 5,4,3,2,1이 출력된다. 즉, 큰 숫자부터 출력이 된다.
for i in range(5):
	print(-heapq.heappop(heap))



# 참고 블로그 https://velog.io/@plate0113/Python-%EC%9A%B0%EC%84%A0%EC%88%9C%EC%9C%84-%ED%81%90-heapq
import heapq

nums = [4, 1, 7, 3, 8, 5]
heap = []

for num in nums:
  heapq.heappush(heap, (-num, num)) 

while heap:
  print(heapq.heappop(heap)[1])
  
  '''
힙에 원소를 추가할때 (-원소의 값,원소의 값)으로 저장을 해준다면
음수의 값으로 최소 힙이 되므로 그 뜻은 원래 양수의 값에서 최대 힙이 된다는 뜻이다.
이런 식으로 조금 응용을 한다면 최대 힙을 구할 수 있다.
  '''
# 최대 힙 
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
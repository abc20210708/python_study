# bisect 라이브러리
from bisect import bisect

my_list = [1, 2, 3, 7, 9, 11, 33]
print(bisect(my_list, 3))

# bisect(<사용할 배열>, 찾을 값)

from bisect import bisect_left, bisect_right
arr = [1, 2, 3, 3, 3, 7, 9, 11, 33]
x = 3

print(f"bisect_left: {bisect_left(arr, x)}")
print(f"bisect_right: {bisect_right(arr, x)}")

'''
bisect_left() 함수는 정렬된 배열에서 
특정 값 x가 삽입될 위치를 반환합니다. 
만약 배열에 이미 x가 존재하는 경우에는 x의 왼쪽 인덱스를 반환합니다.

bisect_right() 함수는 bisect_left() 함수와 거의 동일하지만, 
배열에 이미 x가 존재하는 경우에는 x의 오른쪽 인덱스를 반환합니다.

따라서, 주어진 코드에서 bisect_left(arr, x) 함수는 
x가 삽입될 위치를 찾아 3의 첫 번째 출현 위치를 
나타내는 인덱스 2를 반환합니다. 

마찬가지로, bisect_right(arr, x) 함수는 3이 
마지막으로 출현하는 위치를 나타내는 인덱스 5를 반환합니다.

즉, 3이 주어진 정렬된 배열 arr에서 총 3번 등장하며, 
그 중 첫 번째 등장 위치는 인덱스 2이고, 
마지막 등장 위치는 인덱스 5입니다.
'''
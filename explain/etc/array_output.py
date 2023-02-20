## 참고 블로그 https://covenant.tistory.com/141

# 3-1 배열을 연결해서 출력 1

# map 함수를 이용해 arr에 저장되어 있는
# 정수의 값을 sring 형식으로 변환
arr = [1, 2, 3, 4]
print(''.join(map(str, arr)))


## [1, 2, 3, 4]를 [과 ,를 빼고 출력하려면 어떻게 해야할까요?
# 잘못된 예시
# for num in arr:
#   print(num)

print(*arr)


# 보너스 
'''
3
1 2 3
4 5 6
7 8 9

코딩테스트에서 입력값이 배열로 저장될 법한 값일 때는
항상 몇 개가 주어지는지 알려줍니다. 
위의 입력값에서는 3이 그 역할을 합니다. 
그렇다면 백준 10951 과 같이 끝을 알 수 없는 
입력이 들어온다면 어떻게 해야할까요?
'''

'''
while 1 로 무한히 값을 입력 받아서 EOF 까지 입력받으면 됩니다.

try:
    while 1:
        A, B = map(int, input().split())
        print(A + B)
    except:
        exit()
'''        
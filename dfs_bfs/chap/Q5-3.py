# 재귀 함수 종료 예제 

# 재귀 함수 : 자기 자신을 호출하는 함수
# 재귀 함수를 문 풀이에서 사용할 때는 재귀 함수가 언제 끝날지,
# 종료 조건을 꼭 명시해야한다.




def recursive_function(i) :
    # 100번째 출력했을 때 종료되도록 종료 조건 명시
    if i == 10 :
        return
    print(i, "번째 재귀 함수에서", i + 1, "번째 재귀 함수를 호출합니다.")
    recursive_function(i + 1)
    print(i, '번째 재귀 함수를 종료합니다.')
    
recursive_function(1)





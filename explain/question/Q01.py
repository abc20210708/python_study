'''
/*
    참고 블로그
    https://velog.io/@ji0_0s/Java-369%EA%B2%8C%EC%9E%84-%EC%A7%9C%EB%B3%B4%EA%B8%B0

    * 1부터 100까지의 숫자 중에
    * 1의 자리 숫자가 3,6,9인 경우에 'X'로 표시하고
    * 10단위로 줄바꿈을 하는 프로그램을 만들어보자.
    * */

'''

for i in range(1, 101):
    if i % 10 == 0:
        print(i)
    elif (i % 10) % 3 == 0:
        print("X ", end=" ")
    else:
        print(i, end=" ")
        
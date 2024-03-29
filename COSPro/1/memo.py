## 메모장

## 다른 풀이 - 반복문 활용
#  참고 블로그 https://mag1c.tistory.com/319?category=1125499
def solution(K, words):
    if len(words) == 1: 
        return 1
    res = 1
    size = 0
    for i in range(len(words)):
        if (size + len(words[i]) > K):
            res += 1
            size = 0
        size += len(words[i]) + 1
        
    return res
    

#  참고 블로그 https://jaimemin.tistory.com/2109
def solution(K, words):
    res = 0
    tmp = ""
    
    for word in words:
        if tmp == "":
            tmp = tmp + word
        elif len(tmp+word)+ 1 > K:
            tmp = word
            res +=  1
        else:
            tmp = tmp + "_" + word
        
    if tmp != "":
        res += 1
    
    return res



# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
K = 10
words = ["nice", "happy", "hello", "world", "hi"]
ret = solution(10, words)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
# 문자열 압축

def solution(s):
    answer = len(s)
    # 1개 단위(step)부터 압축 단위를 늘려가며 확인
    for step in range(1, len(s) // 2 + 1):
        res = ""
        prev = s[0:step] #앞에서부터 step만큼의 문자열 추출
        cnt = 1
        
      
        # 단위(step) 크기만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step) :
            # 이전 상태와 동일하다면 압축 횟수(cnt) 증가
            print(f"j :{j}")
            print(f"step : {step}")
            print(f"{j+step}")
            if prev == s[j:j + step]:
                cnt += 1
            # 다른 문자열이 나왔다면(더 이상 압축하지 못하는 경우라면)
            else :
                res += str(cnt) + prev if cnt >= 2 else prev
                prev = s[j:j + step] # 다시 상태 초기화
                cnt = 1
        # 남아 있는 문자열에 대해 처리
        res += str(cnt) + prev if cnt >= 2 else prev
        #만들어지는 압축 문자열이 가장 짧은 것이 정답
        answer = min(answer, len(res))

    return answer

result = solution("abcabcabcabcdededededede")

'''
range함수 매개변수에 숫자를 세개 넣는 경우 range(A, B, C)
A부터 C 숫자만큼의 간격으로 B-1 까지의 정수 범위를 반환합니다. 
B까지가 아닌 B-1 이라는 것에 주의하세요.
'''

## 다른 풀이
def new_solution(s):
    mini = len(s)
    #간격
    for i in range(1,len(s)//2+1):
        q = ''
        cnt = 1
        tmp = s[:i]
        #문자열 인덱스
        for k in range(i,len(s),i):
            #앞에 문자와 같다면
            print(s[k:k+i])
            if s[k:k+i] == tmp:
                cnt +=1
            #앞에 문자와 다르다면, 단 이전것 정리해줘야함.
            else:
                #앞문자와 다른데, cnt에 따라 다르게
                if cnt==1:
                    q += tmp
                else:
                    q+= str(cnt)+tmp
                #tmp 자신으로 바꿔주기
                tmp = s[k:k+i]
                cnt = 1
        if cnt == 1:
            q+=tmp
        else:
            q+= str(cnt)+tmp
        mini = min(mini,len(q))            
    return mini

new_result = new_solution("abcabcdede")
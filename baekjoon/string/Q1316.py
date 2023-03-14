# 그룹 단어 체커

n = int(input())

# 카운트를 처음부터 전체 단어의 개수의 n으로 
# 그룹 단어가 아닐 경우 하나씩 빼는 방식으로 접근

'''
5
ab
aa
aca
ba
bb
'''

cnt = n
for _ in range(n):
    word = input()
    for idx in range(len(word)-1):
        # idx 기준으로 앞뒤 단어가 다를 경우
        if word[idx] != word[idx+1]:
            # idx 뒤쪽 인덱스의 문자열에서
            # word[idx + 1] 문자가 포함되어 있는지 확인
            if word[idx+1] in word[:idx]:
                # 포함되어 있다면 연속해서 알파벳이 나타난게
                # 아니므로 cnt 감소(그룹 단어가 아님)
                cnt -= 1
                # 그리고 break로 for문 탈출 (다음단어로)
                break

print(cnt)
## 단어 나누기 (실버 5)
#  참고 블로그 https://seujang.tistory.com/22

'''
 1. 입력 받은 단어를 세 단어로 나눈다.
 2. 나누어진 단어들을 뒤집는다.
 3. 나누었던 세 단어를 한 단어로 합친다.
 4. 만들었던 단어를 list에 저장해두었다가 
   정렬 후, 가장 첫 단어 출력
'''

word = input()
res = []

for i in range(1, len(word)):
    for j in range(i+1, len(word)):
        part_1 = word[:i][::-1]
        part_2 = word[i:j][::-1]
        part_3 = word[j:][::-1]
        res.append(part_1 + part_2 + part_3)
        
print(sorted(res)[0])
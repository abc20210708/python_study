# 시각 (완전 탐색) - Brute Forcing

'''
00시 00분 00초부터 23시 59분 59초까지 1초씩 늘리면서
시, 분, 초를 문자열 자료형으로 변환하여 합친다.
에) 03시 20분 35초를 확인한다면,
이를 '032035'로 만들어서 '3'이 '032035'에
포함되어 있는지를 체크하는 방식을 이용
'''

hour = 5
cnt = 0

for i in range(hour + 1):
    for j in range(60):
        for k in range(60):
            #매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                cnt += 1


print(cnt)

